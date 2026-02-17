import pygame

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 75
        terrain.x, terrain.y = 0, 0
        terrain.PLAYER_SPEED = 5
        terrain.ModifiedTiles = {
            (2, 2): (255, 0, 0),
            (5, 3): (0, 0, 255),
            (10, 10): (255, 255, 0),
            (-2, -2): (255, 255, 255)
            }

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


        startScreenX = terrain.x // terrain.TILE_SIZE
        startScreenY = terrain.y // terrain.TILE_SIZE
        endScreenX = (terrain.x + terrain.SCREEN_WIDTH) // terrain.TILE_SIZE + 1
        endScreenY = (terrain.y + terrain.SCREEN_HEIGHT) // terrain.TILE_SIZE + 1

        for tileY in range(startScreenY, endScreenY):
            for tileX in range(startScreenX, endScreenX):
                drawX = tileX * terrain.TILE_SIZE - terrain.x
                drawY = tileY * terrain.TILE_SIZE - terrain.y

                if (tileX, tileY) in terrain.ModifiedTiles:
                    color = terrain.ModifiedTiles[(tileX, tileY)]
                else:
                    color = (0, 255, 0)
                    
                pygame.draw.rect(screen, color, (drawX, drawY, terrain.TILE_SIZE, terrain.TILE_SIZE))
                pygame.draw.rect(screen, (0, 200, 0), (drawX, drawY, terrain.TILE_SIZE, terrain.TILE_SIZE), 1)
