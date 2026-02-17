import pygame

class Player:
    def __init__(self):
        self.x = 1280
        self.y = 720
        self.size = 40
        self.speed = 5
        self.health = 100
        self.damage_cooldown = 0
        self.movement_keys = [pygame.K_z,pygame.K_d,pygame.K_s,pygame.K_q]

    def move_player(self,pressed_key):
        if pressed_key[self.movement_keys[0]]:
            self.y -= self.speed
        if pressed_key[self.movement_keys[1]]:
            self.x += self.speed
        if pressed_key[self.movement_keys[2]]:
            self.y += self.speed
        if pressed_key[self.movement_keys[3]]:
            self.x -= self.speed

    def draw_player(self,game):
        pygame.draw.rect(game.screen,"blue",[self.x,self.y,self.size,self.size])