import pygame
pygame.init()
font = pygame.font.Font("assets/fonts/BoldPixels.otf",50)
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
        pygame.draw.rect(screen,"blue",[player.x,player.y,player.SIZE,player.SIZE])

    def draw_player_info(player,screen,heart_image,terrain):
        # Draw health
        pygame.draw.rect(screen,(50,50,50),(50,50,220,70))
        pygame.draw.rect(screen,(150,150,150),(60,60,200,50))
        pygame.draw.rect(screen,(230,50,40),(60,60,2*player.health,50))
        screen.blit(heart_image,(280,50))
        # Draw coordinates
        ajout_coords = len(str(terrain.x//terrain.TILE_SIZE) + str(terrain.y//terrain.TILE_SIZE))-2 
        pygame.draw.rect(screen,(50,50,50),(50,150,200+ajout_coords*25,70))
        pygame.draw.rect(screen,(150,150,150),(60,160,180+ajout_coords*25,50))
        coordinates_text = font.render(f"X:{terrain.x//terrain.TILE_SIZE} Y:{terrain.y//terrain.TILE_SIZE}",True,(225,225,225))
        screen.blit(coordinates_text,(70,160))

        