import pygame

from config import Assets

class InventoryClass:
    def __init__(inventory,game):
        inventory.hotbar = ["sword", "pickaxe", "axe", "hoe", "wood", "stone", "iron_ingot", "iron_nugget", "emerald"]
        inventory.SLOT_SIZE = game.screen.get_rect()[2]//19
        inventory.ratio = inventory.SLOT_SIZE/26 # 26 = Pixel side length of sprite in png file
        inventory.selectedHotbarSlot = 0

        inventory.assets = Assets(inventory.SLOT_SIZE)
        inventory.assets.load_items(inventory.SLOT_SIZE)
        inventory.assets.load_hotbar(inventory.ratio)
        inventory.slot = inventory.assets.HotbarList[0]
        inventory.selectedSlot = inventory.assets.HotbarList[1]
        inventory.EveryBlocks = inventory.assets.Blocks.EveryBlock
        

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
                hoeImage = inventory.EveryBlocks[inventory.hotbar[i]]
                hoeX = inventory.SLOT_SIZE*5 + i*inventory.SLOT_SIZE + (inventory.SLOT_SIZE - hoeImage.get_rect()[2])/2
                hoeY = screen.get_rect()[3]-inventory.SLOT_SIZE-50 + (inventory.SLOT_SIZE - hoeImage.get_rect()[3])/2
                screen.blit(hoeImage,(hoeX,hoeY))
    def select_hotbar_slot(inventory,key):
        inputs = ["&","é",'"',"'","(","-","è","_","ç"]
        for input in inputs:
            if input == key:
                inventory.selectedHotbarSlot = inputs.index(input)
        

        

    

