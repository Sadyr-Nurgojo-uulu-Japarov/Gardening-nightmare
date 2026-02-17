import pygame


class Game:
    def __init__(self):
        # Pygame setup
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((2560, 1440))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gardening nightmares")
        self.running = True

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def draw(self):
        pass


game = Game()
while game.running:
    game.update()
    game.draw()
    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()