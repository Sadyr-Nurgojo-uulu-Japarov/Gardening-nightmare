import pygame

class InventoryClass:
    def __init__(inventory,screen):
        inventory.items = []
        inventory.hotbar = [None]*9
        inventory.SLOT_SIZE = screen.get_rect()[2]//19
        inventory.ratio = inventory.SLOT_SIZE/26 # 26 = Pixel side length of sprite in png file
        inventory.slot = pygame.image.load("assets/Basic_Buttons_3_Fv.png").convert_alpha()
        inventory.slot = pygame.transform.scale(inventory.slot,(576*inventory.ratio,256*inventory.ratio))

    def draw_hotbar(inventory,screen):
        for i in range(9):
            screen.blit(inventory.slot,(inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE,screen.get_rect()[3]-inventory.SLOT_SIZE-50),(235*inventory.ratio,11*inventory.ratio,26*inventory.ratio,24*inventory.ratio))