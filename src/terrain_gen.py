import pygame
import random

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 64
        terrain.x, terrain.y = 0, 0
        terrain.PLAYER_SPEED = 5
        terrain.playerOnTile = False  
        terrain.light_overlay = pygame.Surface((terrain.TILE_SIZE,terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.light_overlay.fill((200, 200, 200, 50))  
        terrain.ModifiedTiles = {}
        terrain.grassTileSet = pygame.image.load("assets/Grass_free.png").convert_alpha()
        terrain.grassTileSet = pygame.transform.scale(terrain.grassTileSet,(576, 64)) # Image size is : 144x16 so we do 144x4=576 and 16x4=64 to get the right size for each tile
        terrain.GrassTypes = {"Plain Grass": (192, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
                              " Grass small foliage": (256, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
                              "Grass foliage": (320, 0, terrain.TILE_SIZE, terrain.TILE_SIZE),
                              "Player On Tile": (384, 0, terrain.TILE_SIZE, terrain.TILE_SIZE)}
        terrain.grass_list = [
            terrain.GrassTypes["Plain Grass"],
            terrain.GrassTypes[" Grass small foliage"],
            terrain.GrassTypes["Grass foliage"],
            terrain.GrassTypes["Player On Tile"]]
        
        # grassImages = ["assets/grass1.png", "assets/grass2.png", "assets/grass3.png"]

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
        playerTileX = (terrain.x + terrain.SCREEN_WIDTH // 2) // terrain.TILE_SIZE
        playerTileY = (terrain.y + terrain.SCREEN_HEIGHT // 2) // terrain.TILE_SIZE

        for tileY in range(startScreenY, endScreenY):
            for tileX in range(startScreenX, endScreenX):
                terrain.playerOnTile = False

                tileSeed = (tileX * 73856093) ^ (tileY * 19349663)
                random.seed(tileSeed)

                tile_index = random.choices([0, 1, 2], weights=[0.95, 0.01, 0.04])[0]
                grassType = terrain.grass_list[tile_index]

                drawX = tileX * terrain.TILE_SIZE - terrain.x
                drawY = tileY * terrain.TILE_SIZE - terrain.y

                if tileX == playerTileX and tileY == playerTileY:
                    terrain.playerOnTile = True

                if (tileX, tileY) in terrain.ModifiedTiles:
                    grassType = terrain.ModifiedTiles[(tileX, tileY)]

                screen.blit(terrain.grassTileSet, (drawX, drawY), grassType)
                pygame.draw.rect(screen, (15, 155, 105), (drawX, drawY, terrain.TILE_SIZE, terrain.TILE_SIZE), 1)

                if terrain.playerOnTile:
                    screen.blit(terrain.light_overlay,(drawX,drawY))

