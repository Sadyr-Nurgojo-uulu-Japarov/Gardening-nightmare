import pygame
from player import Playerfrom enemy import EnemyClass

class Game:
    def __init__(self):
        # Pygame setup
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((2560, 1440))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gardening nightmares")
        self.running = True
        self.enemy1 = EnemyClass(100, 100)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
        player.move_player(pressed_keys)

    def draw(self):
<<<<<<< HEAD
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0), (1280, 720, 50, 50))
        self.enemy1.update()
        self.enemy1.draw(self.screen)
=======
        game.screen.fill("black")
        player.draw_player(game)


game = Game()
player = Player()
while game.running:
    game.update()
    game.draw()
    

    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()