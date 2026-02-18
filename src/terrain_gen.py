import pygame
import random
from opensimplex import OpenSimplex

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 64
        terrain.PLAYER_SPEED = 10
        terrain.x, terrain.y = 0, 0
        terrain.tmp_noise = OpenSimplex(seed=random.randint(0, 1000000))
        terrain.light_overlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.light_overlay.fill((200, 200, 200, 50))  
        terrain.mouseHighlightOverlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.mouseHighlightOverlay.fill((255, 255, 255, 100)) 
        terrain.ModifiedTiles = {}

        terrain.GrassList = []
        for i in range(9):
            path = f"assets/grass/grass{i}.png"
            img = pygame.image.load(path).convert_alpha()
            terrain.GrassList.append(pygame.transform.scale(img, (terrain.TILE_SIZE, terrain.TILE_SIZE)))

        farmland_path = "assets/grassfarmland/grassfarmland92.png"
        farmland_raw = pygame.image.load(farmland_path).convert_alpha()
        terrain.farmland_img = pygame.transform.scale(farmland_raw, (terrain.TILE_SIZE, terrain.TILE_SIZE))
        
        terrain.HerbsFarmlandTypes = {
            "farmland": terrain.farmland_img
        }

        terrain.NatureList = []
        for i in range(5):
            path = f"assets/nature/nature{i}.png"
            img = pygame.image.load(path).convert_alpha()
            terrain.NatureList.append(pygame.transform.scale(img, (terrain.TILE_SIZE, terrain.TILE_SIZE)))
        
        terrain.TreesList = []
        for i in range(2, 5):
            path = f"assets/tree/tree{i}.png"
            img = pygame.image.load(path).convert_alpha()
            terrain.TreesList.append(pygame.transform.scale(img, (terrain.TILE_SIZE * 2, terrain.TILE_SIZE * 3)))

    def move_player(terrain, keys):
        terrain.rocks = pygame.image.load
        nerf = 1
        k = [keys[pygame.K_d],keys[pygame.K_q],keys[pygame.K_z],keys[pygame.K_s]]
        n = 0
        for i in k:
            if i:
                n += 1
        if n == 2:
            nerf = (((terrain.PLAYER_SPEED**2)/2)**0.5)/terrain.PLAYER_SPEED 
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

        startScreenX = int(terrain.x // terrain.TILE_SIZE)
        startScreenY = int(terrain.y // terrain.TILE_SIZE)
        endScreenX = int((terrain.x + terrain.SCREEN_WIDTH) // terrain.TILE_SIZE) + 1
        endScreenY = int((terrain.y + terrain.SCREEN_HEIGHT) // terrain.TILE_SIZE) + 1
        
        playerTileX = (terrain.x + terrain.SCREEN_WIDTH // 2) // terrain.TILE_SIZE
        playerTileY = (terrain.y + terrain.SCREEN_HEIGHT // 2) // terrain.TILE_SIZE

        mouseTileX = (terrain.x + pygame.mouse.get_pos()[0]) // terrain.TILE_SIZE
        mouseTileY = (terrain.y + pygame.mouse.get_pos()[1]) // terrain.TILE_SIZE

        for tileY in range(startScreenY, endScreenY):
            for tileX in range(startScreenX, endScreenX):
                
                drawX = tileX * terrain.TILE_SIZE - terrain.x
                drawY = tileY * terrain.TILE_SIZE - terrain.y

                if (tileX, tileY) in terrain.ModifiedTiles:
                    screen.blit(terrain.ModifiedTiles[(tileX, tileY)], (drawX, drawY))
                else:
                    val = terrain.tmp_noise.noise2(tileX * biomeScale, tileY * biomeScale)
                    
                    if val < -0.333:
                        base_offset = 0
                    elif val < 0.333:
                        base_offset = 3
                    else:
                        base_offset = 6

                    random.seed((tileX * 73856093) ^ (tileY * 19349663))
                    foliage_choice = random.choices([0, 1, 2], weights=[0.90, 0.07, 0.03])[0]
                    finalIndex = base_offset + foliage_choice
                    
                    screen.blit(terrain.GrassList[finalIndex], (drawX, drawY))

                random.seed((tileX * 19349663) ^ (tileY * 73856093))

                if (tileX, tileY) not in terrain.ModifiedTiles and not base_offset == 0 and not base_offset == 6:
                    spawnType = random.choices(["nothing", "nature", "tree"], weights=[0.98, 0.01, 0.01])[0]

                    if spawnType == "nature":
                        nature_choice = random.choice(terrain.NatureList)
                        screen.blit(nature_choice, (drawX, drawY))
                    elif spawnType == "tree":
                        tree_choice = random.choice(terrain.TreesList)
                        screen.blit(tree_choice, (drawX - terrain.TILE_SIZE, drawY - terrain.TILE_SIZE*2))

                if tileX == playerTileX and tileY == playerTileY:
                    screen.blit(terrain.light_overlay, (drawX, drawY))
                
                if tileX == mouseTileX and tileY == mouseTileY:
                    screen.blit(terrain.mouseHighlightOverlay, (drawX, drawY))