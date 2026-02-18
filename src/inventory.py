import pygame

class InventoryClass:
    def __init__(inventory,game):
        inventory.items = ["Hoe"]
        inventory.hotbar = ["Hoe","Sword"] + [None]*7
        inventory.SLOT_SIZE = game.screen.get_rect()[2]//19
        inventory.ratio = inventory.SLOT_SIZE/26 # 26 = Pixel side length of sprite in png file
        inventory.slot = pygame.image.load("assets/hotbar_slot.png").convert_alpha()
        inventory.slot = pygame.transform.scale(inventory.slot,(26*inventory.ratio,26*inventory.ratio))
        inventory.selectedSlot = pygame.image.load("assets/selected_hotbar_slot.png").convert_alpha()
        inventory.selectedSlot = pygame.transform.scale(inventory.selectedSlot,(26*inventory.ratio,26*inventory.ratio))
        inventory.selectedHotbarSlot = 0
        # Loading all object sprites AW GAAAWWWD
        hoe_image = pygame.image.load("assets/item/hoe.png").convert_alpha()
        hoe_image = pygame.transform.scale(hoe_image,(inventory.SLOT_SIZE*0.7,inventory.SLOT_SIZE*0.7))
        sword_image = pygame.image.load("assets/item/sword.png").convert_alpha()
        sword_image = pygame.transform.scale(sword_image,(inventory.SLOT_SIZE*0.6,inventory.SLOT_SIZE*0.6))
        sword_image = pygame.transform.rotate(sword_image,-45)
        inventory.AllObjects = {"Hoe":hoe_image,"Sword":sword_image}
        

    def draw_hotbar(inventory,screen):
        for i in range(9):
            x = inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE
            y = screen.get_rect()[3]-inventory.SLOT_SIZE-50
            if i == inventory.selectedHotbarSlot:
                screen.blit(inventory.selectedSlot,(x,y))
            else:
                screen.blit(inventory.slot,(x,y))
            if inventory.hotbar[i] is None:
                pass
            else:
                hoeImage = inventory.AllObjects[inventory.hotbar[i]]
                hoeX = inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE + (inventory.SLOT_SIZE - hoeImage.get_rect()[2])/2
                hoeY = screen.get_rect()[3]-inventory.SLOT_SIZE-50 + (inventory.SLOT_SIZE - hoeImage.get_rect()[3])/2
                screen.blit(hoeImage,(hoeX,hoeY))
    def select_hotbar_slot(inventory,key):
        inputs = ["&","é",'"',"'","(","-","è","_","ç"]
        for input in inputs:
            if input == key:
                inventory.selectedHotbarSlot = inputs.index(input)
        

        

    

