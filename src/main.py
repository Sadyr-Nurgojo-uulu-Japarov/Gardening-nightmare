import pygame
from player import PlayerClass
from enemy import EnemyClass
from terrain_gen import TerrainGenClass
from inventory import InventoryClass

class GameClass:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.screen.get_size()
        pygame.mouse.set_visible(False)
        
        #loading images
        self.heart_image = pygame.image.load("assets/heart.png").convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image,(75,75))
        self.cursor = pygame.image.load("assets/Mouse_cursors.png").convert_alpha()
        self.cursor = pygame.transform.scale(self.cursor,(384,128))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gardening nightmares")
        self.running = True
        self.terrain = TerrainGenClass(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player = PlayerClass(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.enemy1 = EnemyClass(100, 100, self.player, self.terrain)
        self.inventory = InventoryClass(self.screen)
        

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.health -= 5
        self.terrain.move_player(pressed_keys)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.enemy1.update()
        self.terrain.draw_terrain(self.screen)
        self.enemy1.draw(self.screen)
        self.player.draw_player(self.screen)
        self.player.draw_player_info(self.screen,self.heart_image,self.terrain)
        self.draw_mouse()
        self.inventory.draw_hotbar(self.screen)


    def draw_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.cursor,mouse_pos,(208,12,32,40))
        

game = GameClass()

while game.running:
    game.update()
    game.draw()
    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()