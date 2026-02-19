import pygame  # python.exe -m pip install pygame-ce
from player import PlayerClass
from enemy import EnemyClass
from terrain_gen import TerrainGenClass
from inventory import InventoryClass
from config import Assets

class GameClass:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, vsync=1)

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.screen.get_size()
        pygame.mouse.set_visible(False)
        
        self.assets = Assets()
        self.assets.load_cursor()
        #loading images
        self.heartImage = pygame.image.load("assets/heart.png").convert_alpha()
        self.heartImage = pygame.transform.scale(self.heartImage,(75,75))

        

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gardening nightmares")
        self.running = True
        self.terrain = TerrainGenClass(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player = PlayerClass(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.enemy = EnemyClass(100, 100, self.player, self.terrain)
        self.inventory = InventoryClass(self)
        

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #event.button = 1 is left click
                if self.inventory.hotbar[self.inventory.selectedHotbarSlot] == "Hoe":
                    self.terrain.modify_tile(pygame.mouse.get_pos(), "farmland")
                elif self.inventory.hotbar[self.inventory.selectedHotbarSlot] == "Sword" and self.player.swingCooldown == 0:
                    self.player.isSwinging = True
            elif event.type == pygame.TEXTINPUT:
                self.inventory.select_hotbar_slot(event.text)
        self.terrain.move_player(pressed_keys)
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.enemy.update()
        self.terrain.draw_terrain(self.screen)
        self.enemy.draw(self.screen)
        self.player.draw_player(self.screen)
        self.player.draw_held_tool(self.screen,self.inventory.AllObjects,
                                   self.inventory.hotbar[self.inventory.selectedHotbarSlot])
        self.player.draw_player_info(self.screen,self.heartImage,self.terrain)
        self.inventory.draw_hotbar(self.screen)
        self.draw_mouse()

    def draw_mouse(self):
        mousePos = pygame.mouse.get_pos()
        self.screen.blit(self.assets.cursor, mousePos,(52 * self.assets.CURSOR_SIZE_FACTOR, 3 * self.assets.CURSOR_SIZE_FACTOR,
                                                8 * self.assets.CURSOR_SIZE_FACTOR, 10 * self.assets.CURSOR_SIZE_FACTOR))
        

game = GameClass()

while game.running:
    game.update()
    game.draw()
    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()