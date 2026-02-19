import pygame
import random
from opensimplex import OpenSimplex
from config import Assets

class TerrainGenClass:
    def __init__(terrain, screen_width, screen_height):
        terrain.SCREEN_WIDTH = screen_width
        terrain.SCREEN_HEIGHT = screen_height
        terrain.TILE_SIZE = 64
        terrain.PLAYER_SPEED = 10
        terrain.x, terrain.y = 0, 0
        terrain.tmpNoiseBiomes = OpenSimplex(seed=random.randint(0, 1000000))
        terrain.tmpNoiseWater = OpenSimplex(seed=random.randint(0, 1000000))
        terrain.lightOverlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.lightOverlay.fill((200, 200, 200, 50))  
        terrain.mouseHighlightOverlay = pygame.Surface((terrain.TILE_SIZE, terrain.TILE_SIZE), pygame.SRCALPHA)
        terrain.mouseHighlightOverlay.fill((255, 255, 255, 100)) 
        terrain.ModifiedTiles = {}

        terrain.assets = Assets(terrain.TILE_SIZE)
        terrain.assets.load_grass() # Get an image : terrain.assets.GrassList[index]
        terrain.assets.load_farmland()
        terrain.assets.load_nature()
        terrain.assets.load_tree()
        terrain.assets.load_lake()


    def move_player(terrain, keys):
        nerf = 1
        keysPressed = [keys[pygame.K_d],keys[pygame.K_q],keys[pygame.K_z],keys[pygame.K_s]]
        pressedKeysNumber = 0
        for keyIsPressed in keysPressed:
            if keyIsPressed:
                pressedKeysNumber += 1
        if pressedKeysNumber == 2:
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

    def modify_tile(terrain, mousePos, newTileType):
        tileX = (terrain.x + mousePos[0]) // terrain.TILE_SIZE
        tileY = (terrain.y + mousePos[1]) // terrain.TILE_SIZE
        if (tileX, tileY) in terrain.ModifiedTiles:
            return 
        elif newTileType == "farmland":
            terrain.ModifiedTiles[(tileX, tileY)] = terrain.assets.Blocks.EveryBlock["farmland"]

    def draw_terrain(terrain, screen):
        biomeScale = 0.04

        startScreenX = int(terrain.x // terrain.TILE_SIZE)
        startScreenY = int(terrain.y // terrain.TILE_SIZE)
        endScreenX = int((terrain.x + terrain.SCREEN_WIDTH) // terrain.TILE_SIZE) + 2
        endScreenY = int((terrain.y + terrain.SCREEN_HEIGHT) // terrain.TILE_SIZE) + 3
        
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
                    noiseValueBiome = terrain.tmpNoiseBiomes.noise2(tileX * biomeScale, tileY * biomeScale)
                    
                    if noiseValueBiome < -0.333:
                        baseOffset = 0
                    elif noiseValueBiome < 0.333:
                        baseOffset = 3
                    else:
                        baseOffset = 6

                    noiseValueWater = terrain.tmpNoiseWater.noise2(tileX * biomeScale * 2, tileY * biomeScale * 2)
                    if noiseValueWater < -0.6 and baseOffset == 0:
                        random.seed((tileX * 1936292**3) ^ (tileY * 734756457593))
                        screen.blit(terrain.assets.LakeList[random.choices([0, 1, 2], weights=[0.8, 0.15, 0.05])[0]], (drawX, drawY))
                        if tileX == playerTileX and tileY == playerTileY:
                            screen.blit(terrain.lightOverlay, (drawX, drawY))
                
                        if tileX == mouseTileX and tileY == mouseTileY:
                            screen.blit(terrain.mouseHighlightOverlay, (drawX, drawY))
                        continue

                    random.seed((tileX * 73856093) ^ (tileY * 19349663))
                    foliageChoice = random.choices([0, 1, 2], weights=[0.90, 0.07, 0.03])[0]
                    finalIndex = baseOffset + foliageChoice
                    
                    screen.blit(terrain.assets.GrassList[finalIndex], (drawX, drawY))

                random.seed((tileX * 19349663) ^ (tileY * 73856093))

                if (tileX, tileY) not in terrain.ModifiedTiles and not baseOffset == 0 and not baseOffset == 6:
                    spawnType = random.choices(["nothing", "nature", "tree"], weights=[0.98, 0.01, 0.01])[0]

                    if spawnType == "nature":
                        natureChoice = random.choice(terrain.assets.NatureList)
                        screen.blit(natureChoice, (drawX, drawY))
                    elif spawnType == "tree":
                        treeChoice = random.choice(terrain.assets.TreesList)
                        screen.blit(treeChoice, (drawX - terrain.TILE_SIZE, drawY - terrain.TILE_SIZE*2))

                if tileX == playerTileX and tileY == playerTileY:
                    screen.blit(terrain.lightOverlay, (drawX, drawY))
                
                if tileX == mouseTileX and tileY == mouseTileY:
                    screen.blit(terrain.mouseHighlightOverlay, (drawX, drawY))
                
                