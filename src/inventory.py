import pygame

class InventoryClass:
    def __init__(inventory,screen):
        inventory.items = []
        inventory.hotbar = [None]*9
        inventory.SLOT_SIZE = screen.get_rect()[2]//19
        inventory.slot = pygame.image.load("assets/Basic_Buttons_3_Fv.png").convert_alpha()
        inventory.slot = pygame.transform.scale(inventory.slot,(1152,512))

    def draw_hotbar(inventory,screen):
        for i in range(9):
            screen.blit(inventory.slot,(inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE,screen.get_rect()[3]-inventory.SLOT_SIZE-20),(470,22,52,48))