import pygame

class InventoryClass:
    def __init__(inventory,screen):
        inventory.items = ["Hoe"]
        inventory.hotbar = ["Hoe"] + [None]*8
        inventory.SLOT_SIZE = screen.get_rect()[2]//19
        inventory.ratio = inventory.SLOT_SIZE/26 # 26 = Pixel side length of sprite in png file
        inventory.slot = pygame.image.load("assets/Basic_Buttons_3_Fv.png").convert_alpha()
        inventory.slot = pygame.transform.scale(inventory.slot,(576*inventory.ratio,256*inventory.ratio))

        # Loading all object sprites AW GAAAWWWD
        hoe_image = pygame.image.load("assets/item/hoe.png").convert_alpha()
        hoe_image = pygame.transform.scale(hoe_image,(inventory.SLOT_SIZE*0.7,inventory.SLOT_SIZE*0.7))
        hoe_image = pygame.transform.rotate(hoe_image,-45)
        inventory.AllObjects = {"Hoe":hoe_image}

    def draw_hotbar(inventory,screen):
        for i in range(9):
            screen.blit(inventory.slot,(inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE,screen.get_rect()[3]-inventory.SLOT_SIZE-50),(235*inventory.ratio,11*inventory.ratio,26*inventory.ratio,24*inventory.ratio))
            if inventory.hotbar[i] is None:
                pass
            else:
                print((inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE+inventory.SLOT_SIZE//10,screen.get_rect()[3]-inventory.SLOT_SIZE-40),pygame.mouse.get_pos())
                screen.blit(inventory.AllObjects["Hoe"],(inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE+inventory.SLOT_SIZE//10,screen.get_rect()[3]-inventory.SLOT_SIZE-40))

