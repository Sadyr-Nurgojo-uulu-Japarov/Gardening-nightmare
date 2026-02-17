import pygame

# Pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1440,900))
clock = pygame.time.Clock()
pygame.display.set_caption("Gardening nightmares")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    clock.tick(60)
pygame.quit()