import pygame
from player import PlayerClass
from enemy import EnemyClass
from terrain_gen import TerrainGenClass

class GameClass:
    def __init__(self):
        # Pygame setup
        pygame.init()
        pygame.mixer.init()
        info = pygame.display.Info()
 
        self.SCREEN_WIDTH = info.current_w
        self.SCREEN_HEIGHT = info.current_h

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gardening nightmares")
        self.running = True
        self.player = PlayerClass()
        self.enemy1 = EnemyClass(100, 100,self.player)
        self.terrain = TerrainGenClass()
        self.terrain.generate_terrain()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
        self.player.move_player(pressed_keys)

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0), (1280, 720, 50, 50))
        self.enemy1.update()
        self.terrain.draw_terrain(self.screen)
        self.enemy1.draw(self.screen)
        self.player.draw_player(self.screen)
        


game = GameClass()

while game.running:
    game.update()
    game.draw()

    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()