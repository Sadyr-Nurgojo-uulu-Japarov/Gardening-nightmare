import pygame

class PlayerClass:
    def __init__(player, screen_width, screen_height):
        player.SCREEN_WIDTH = screen_width
        player.SCREEN_HEIGHT = screen_height
        player.SIZE = 40
        player.health = 100
        player.damage_cooldown = 0
        player.x = player.SCREEN_WIDTH//2 - player.SIZE // 2 
        player.y = player.SCREEN_HEIGHT//2 - player.SIZE // 2
        

    def draw_player(player,screen):
        pygame.draw.rect(screen, "blue", (player.x, player.y, player.SIZE, player.SIZE))