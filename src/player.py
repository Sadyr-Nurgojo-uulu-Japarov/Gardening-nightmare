import pygame

class PlayerClass:
    def __init__(player):
        player.x = 1280
        player.y = 720
        player.size = 40
        player.speed = 5
        player.health = 100
        player.damage_cooldown = 0
        player.movement_keys = [pygame.K_z,pygame.K_d,pygame.K_s,pygame.K_q]

    def move_player(player,pressed_key):
        if pressed_key[player.movement_keys[0]]:
            player.y -= player.speed
        if pressed_key[player.movement_keys[1]]:
            player.x += player.speed
        if pressed_key[player.movement_keys[2]]:
            player.y += player.speed
        if pressed_key[player.movement_keys[3]]:
            player.x -= player.speed

    def draw_player(player,screen):
        pygame.draw.rect(screen,"blue",[player.x,player.y,player.size,player.size])