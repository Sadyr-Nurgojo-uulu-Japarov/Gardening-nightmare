import pygame
pygame.init()
font = pygame.font.Font("assets/fonts/BoldPixels.otf",50)
class PlayerClass:
    def __init__(player, screen_width, screen_height):
        player.SCREEN_WIDTH, player.SCREEN_HEIGHT = screen_width, screen_height
        player.position = pygame.Vector2(screen_width // 2, screen_height // 2)
        player.SIZE = 40
        player.health = 100
        player.item_index = 8 
        player.font = pygame.font.SysFont("Arial", 30, bold=True)
        player.items = []
        itemTileSet = pygame.image.load("assets/Items_free.png").convert_alpha()
        for i in range(10): # On découpe les 10 premiers items
            surf = pygame.Surface((16, 16), pygame.SRCALPHA)
            surf.blit(itemTileSet, (0, 0), (i * 16, 0, 16, 16))
            player.items.append(pygame.transform.scale(surf, (player.SIZE, player.SIZE)))

    def draw_player(player,screen,item_image):

        item_image = pygame.transform.scale(item_image,(player.SIZE * 9,player.SIZE))

        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        direction = mouse_pos - player.position
        angle = direction.angle_to(pygame.Vector2(1, 0))
        item_rotated = pygame.transform.rotate(player.items[player.item_index], angle - 90)
         
        orbit_offset = pygame.Vector2(60, 0).rotate(-angle)
        item_rect = item_rotated.get_rect(center=player.position + orbit_offset)

        
        pygame.draw.rect(screen,"blue",[player.position.x-player.SIZE//2,player.position.y-player.SIZE//2,player.SIZE,player.SIZE])
        screen.blit(item_rotated,item_rect)




    def draw_player_info(player,screen,heart_image,terrain):
        # Draw health
        pygame.draw.rect(screen,(50,50,50),(50,50,220,70))
        pygame.draw.rect(screen,(150,150,150),(60,60,200,50))
        pygame.draw.rect(screen,(230,50,40),(60,60,2*player.health,50))
        screen.blit(heart_image,(280,50))
        # Draw coordinates
        x = terrain.x//terrain.TILE_SIZE
        y = terrain.y//terrain.TILE_SIZE
        ajout_coords = len(str(x) + str(y))-2 
        pygame.draw.rect(screen,(50,50,50),(50,150,200+ajout_coords*25,70))
        pygame.draw.rect(screen,(150,150,150),(60,160,180+ajout_coords*25,50))
        coordinates_text = font.render(f"X:{x} Y:{y}",True,(225,225,225))
        screen.blit(coordinates_text,(70,160))

