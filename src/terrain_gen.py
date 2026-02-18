import pygame
import random
from opensimplex import OpenSimplex

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 64
        RAW_ART_TILE_SIZE = 16
        terrain.PLAYER_SPEED = 5
        terrain.x, terrain.y = 0, 0
        terrain.tmp_noise = OpenSimplex(seed=random.randint(0, 1000000))
        terrain.light_overlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.light_overlay.fill((200, 200, 200, 50))  
        terrain.ModifiedTiles = {}
        terrain.grassTileSet = pygame.image.load("assets/Grass_free.png").convert_alpha()
        terrain.IMAGE_SIZE_FACTOR = terrain.TILE_SIZE / RAW_ART_TILE_SIZE
        original_w = terrain.grassTileSet.get_width()
        original_h = terrain.grassTileSet.get_height()
        terrain.grassTileSet = pygame.transform.scale(
            terrain.grassTileSet, 
            (int(original_w * terrain.IMAGE_SIZE_FACTOR), int(original_h * terrain.IMAGE_SIZE_FACTOR)))
        f = terrain.IMAGE_SIZE_FACTOR # To make reading easier
        # Instead of 0, 48, 192, we use (TileIndex * 16 pixels * scale)
        terrain.GrassTypes = {
            "Light Green Grass": (0 * RAW_ART_TILE_SIZE * f, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
            "Grass":             (3 * RAW_ART_TILE_SIZE * f, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
            "Dark Grass":        (6 * RAW_ART_TILE_SIZE * f, 0, terrain.TILE_SIZE, terrain.TILE_SIZE)}
        terrain.GrassList = [
            terrain.GrassTypes["Light Green Grass"],
            terrain.GrassTypes["Grass"],
            terrain.GrassTypes["Dark Grass"]]

    def move_player(terrain, keys):
        if keys[pygame.K_d]:
            terrain.x += terrain.PLAYER_SPEED
        if keys[pygame.K_q]:
            terrain.x -= terrain.PLAYER_SPEED
        if keys[pygame.K_z]:
            terrain.y -= terrain.PLAYER_SPEED
        if keys[pygame.K_s]:
            terrain.y += terrain.PLAYER_SPEED

    def draw_terrain(terrain, screen):
        biomeScale = 0.03

        startScreenX = terrain.x // terrain.TILE_SIZE
        startScreenY = terrain.y // terrain.TILE_SIZE
        endScreenX = (terrain.x + terrain.SCREEN_WIDTH) // terrain.TILE_SIZE + 1
        endScreenY = (terrain.y + terrain.SCREEN_HEIGHT) // terrain.TILE_SIZE + 1
        
        playerTileX = (terrain.x + terrain.SCREEN_WIDTH // 2) // terrain.TILE_SIZE
        playerTileY = (terrain.y + terrain.SCREEN_HEIGHT // 2) // terrain.TILE_SIZE

        for tileY in range(startScreenY, endScreenY):
            for tileX in range(startScreenX, endScreenX):
                
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

                grassType = (base_rect[0] + grassFoliage, base_rect[1], base_rect[2], base_rect[3])

                drawX = tileX * terrain.TILE_SIZE - terrain.x
                drawY = tileY * terrain.TILE_SIZE - terrain.y

                if (tileX, tileY) in terrain.ModifiedTiles:
                    grassType = terrain.ModifiedTiles[(tileX, tileY)]

                screen.blit(terrain.grassTileSet, (drawX, drawY), grassType)

                if tileX == playerTileX and tileY == playerTileY:
                    screen.blit(terrain.light_overlay, (drawX, drawY))