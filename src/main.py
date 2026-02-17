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
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
        player.move_player(pressed_keys)

    def draw(self):
        game.screen.fill("black")
        player.draw_player()

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
        print(pressed_key)
        if pressed_key[self.movement_keys[0]]:
            self.y -= self.speed
        if pressed_key[self.movement_keys[1]]:
            self.x += self.speed
        if pressed_key[self.movement_keys[2]]:
            self.y += self.speed
        if pressed_key[self.movement_keys[3]]:
            self.x -= self.speed

    def draw_player(self):
        pygame.draw.rect(game.screen,"blue",[self.x,self.y,self.size,self.size])

game = Game()
player = Player()
while game.running:
    game.update()
    game.draw()
    pygame.display.flip()
    game.clock.tick(60)
pygame.quit()