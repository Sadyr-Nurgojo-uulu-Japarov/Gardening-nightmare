import pygame


class TerrainGenClass:
    def __init__(terrain):
        terrain.map = []

    def generate_terrain(terrain):
        for i in range(0, 2560, 50):
            for j in range(0, 1440, 50):
                terrain.map.append((i, j, 1 if i % 100 == 0 else 0, 1 if j % 100 == 0 else 0))
                

    def draw_terrain(terrain, screen):
        for tile in terrain.map:
            color = (34, 135, 34) if tile[2] == tile[3] else (34, 130, 34)
            pygame.draw.rect(screen, color, (tile[0], tile[1], 50, 50))


# Noise terrain generation for the future