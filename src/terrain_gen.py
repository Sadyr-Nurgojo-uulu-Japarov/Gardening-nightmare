import pygame
import random
from opensimplex import OpenSimplex

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 64
        RAW_ART_TILE_SIZE = 16
        terrain.PLAYER_SPEED = 10
        terrain.x, terrain.y = 0, 0
        terrain.tmp_noise = OpenSimplex(seed=random.randint(0, 1000000))
        terrain.light_overlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.light_overlay.fill((200, 200, 200, 50))  
        terrain.mouseHighlightOverlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.mouseHighlightOverlay.fill((255, 255, 255, 100)) 
        terrain.ModifiedTiles = {}


        terrain.grassTileSet = pygame.image.load("assets/Grass_free.png").convert_alpha()
        terrain.grassTileSetSIZE_FACTOR = terrain.TILE_SIZE / RAW_ART_TILE_SIZE
        terrain.grassTileSet = pygame.transform.scale(terrain.grassTileSet,
            (int(terrain.grassTileSet.get_width() * terrain.grassTileSetSIZE_FACTOR),
             int(terrain.grassTileSet.get_height() * terrain.grassTileSetSIZE_FACTOR)))
        gts_SF = terrain.grassTileSetSIZE_FACTOR # To make reading easier
        # Instead of 0, 48, 192, we use (TileIndex * 16 pixels * scale)
        terrain.GrassTypes = {
            "Light Green Grass": (0 * RAW_ART_TILE_SIZE * gts_SF, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
            "Grass":             (3 * RAW_ART_TILE_SIZE * gts_SF, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
            "Dark Grass":        (6 * RAW_ART_TILE_SIZE * gts_SF, 0, terrain.TILE_SIZE, terrain.TILE_SIZE)}
        terrain.GrassList = [
            terrain.GrassTypes["Light Green Grass"],
            terrain.GrassTypes["Grass"],
            terrain.GrassTypes["Dark Grass"]]
        

        terrain.herbsFarmlandTileSet = pygame.image.load("assets/herbs_farmland.png").convert_alpha()
        terrain.herbsFarmlandTileSetSIZE_FACTOR = terrain.TILE_SIZE / RAW_ART_TILE_SIZE
        terrain.herbsFarmlandTileSet = pygame.transform.scale((terrain.herbsFarmlandTileSet),
             (int(terrain.herbsFarmlandTileSet.get_width() * terrain.herbsFarmlandTileSetSIZE_FACTOR), int(terrain.herbsFarmlandTileSet.get_height() * terrain.herbsFarmlandTileSetSIZE_FACTOR)))
        hfts_SF = terrain.herbsFarmlandTileSetSIZE_FACTOR # To make reading easier
        terrain.HerbsFarmlandTypes = {
            "farmland": [terrain.herbsFarmlandTileSet, (192 * RAW_ART_TILE_SIZE * hfts_SF, 80 * RAW_ART_TILE_SIZE * hfts_SF, terrain.TILE_SIZE, terrain.TILE_SIZE)]}


    def move_player(terrain, keys):
        nerf = 1
        k = [keys[pygame.K_d],keys[pygame.K_q],keys[pygame.K_z],keys[pygame.K_s]]
        n = 0
        for i in k:
            if i:
                n += 1
        if n == 2:
            nerf = (((terrain.PLAYER_SPEED**2)/2)**0.5)/terrain.PLAYER_SPEED # Approximation using pythagorean Theorem to not change speed while going diagonal
        if keys[pygame.K_d]:
            terrain.x += terrain.PLAYER_SPEED*nerf
        if keys[pygame.K_q]:
            terrain.x -= terrain.PLAYER_SPEED*nerf
        if keys[pygame.K_z]:
            terrain.y -= terrain.PLAYER_SPEED*nerf
        if keys[pygame.K_s]:
            terrain.y += terrain.PLAYER_SPEED*nerf
        terrain.x,terrain.y = round(terrain.x),round(terrain.y)

    def modify_tile(terrain, mouse_pos, new_tile_type):
        tileX = (terrain.x + mouse_pos[0]) // terrain.TILE_SIZE
        tileY = (terrain.y + mouse_pos[1]) // terrain.TILE_SIZE
        if (tileX, tileY) in terrain.ModifiedTiles:
            return 
        elif new_tile_type == "farmland":
            terrain.ModifiedTiles[(tileX, tileY)] = terrain.HerbsFarmlandTypes["farmland"]


    def draw_terrain(terrain, screen):
        biomeScale = 0.03

        startScreenX = terrain.x // terrain.TILE_SIZE
        startScreenY = terrain.y // terrain.TILE_SIZE
        endScreenX = (terrain.x + terrain.SCREEN_WIDTH) // terrain.TILE_SIZE + 1
        endScreenY = (terrain.y + terrain.SCREEN_HEIGHT) // terrain.TILE_SIZE + 1
        
        playerTileX = (terrain.x + terrain.SCREEN_WIDTH // 2) // terrain.TILE_SIZE
        playerTileY = (terrain.y + terrain.SCREEN_HEIGHT // 2) // terrain.TILE_SIZE

        mouseTileX = (terrain.x + pygame.mouse.get_pos()[0]) // terrain.TILE_SIZE
        mouseTileY = (terrain.y + pygame.mouse.get_pos()[1]) // terrain.TILE_SIZE

        for tileY in range(startScreenY, endScreenY):
            for tileX in range(startScreenX, endScreenX):
                
                

                drawX = tileX * terrain.TILE_SIZE - terrain.x
                drawY = tileY * terrain.TILE_SIZE - terrain.y

                if (tileX, tileY) in terrain.ModifiedTiles:
                    tileType = terrain.ModifiedTiles[(tileX, tileY)]
                    screen.blit(tileType[0], (drawX, drawY), tileType[1])
                    tileType = tileType[1]
                else:
                    # 1. Biome Selection
                    val = terrain.tmp_noise.noise2(tileX * biomeScale, tileY * biomeScale)
                    if val < -0.333:
                        tile_index = 0
                    elif val < 0.333:
                        tile_index = 1 
                    else:
                        tile_index = 2 

                    base_rect = terrain.GrassList[tile_index]

                    random.seed((tileX * 73856093) ^ (tileY * 19349663))

                    step = terrain.TILE_SIZE 
                    grassFoliage = random.choices([0, step, step * 2], weights=[0.95, 0.02, 0.03])[0]

                    tileType = (base_rect[0] + grassFoliage, base_rect[1], base_rect[2], base_rect[3])
                    screen.blit(terrain.grassTileSet, (drawX, drawY), tileType)

                if tileX == playerTileX and tileY == playerTileY:
                    screen.blit(terrain.light_overlay, (drawX, drawY))
                
                if tileX == mouseTileX and tileY == mouseTileY:
                    screen.blit(terrain.mouseHighlightOverlay, (drawX, drawY))