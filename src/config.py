import pygame

class Assets:
    def __init__(self, TILE_SIZE=16):
        self.TILE_SIZE = TILE_SIZE
        self.Blocks = Block()
        self.Objects = Objects()

    def load_grass(self):
        self.GrassList = []
        grassNames = ["sparse bright grass", "medium bright grass", "dense bright grass",
                      "sparse meadow grass", "medium meadow grass", "dense meadow grass",
                      "sparse wild grass", "medium wild grass", "dense wild grass"]
        for i in range(len(grassNames)):
            if grassNames[i] == "none":
                continue
            path = f"assets/grass/grass{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.GrassList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(grassNames[i])] = self.GrassList[-1]

    def load_farmland(self):
        """
        self.FarmlandList = []
        farmlandNames = ["farmland"]
        for i in range(len(farmlandNames)):
            if farmlandNames[i] == "none":
                continue
            path = f"assets/grassfarmland/grassfarmland{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.FarmlandList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(farmlandNames[i])] = self.FarmlandList[-1]
            """
        img = pygame.image.load("assets/grassfarmland/grassfarmland92.png").convert_alpha()
        self.farmland = pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE))
        self.Blocks.EveryBlock["farmland"] = self.farmland

    def load_nature(self):
        self.NatureList = []
        natureNames = ["rock", "none", "none", "bush", "trunk"]
        for i in range(len(natureNames)):
            if natureNames[i] == "none":
                continue
            path = f"assets/nature/nature{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.NatureList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(natureNames[i])] = self.NatureList[-1]

    def load_tree(self):
        self.TreesList = []
        treeNames = ["none", "none", "small tree", "big tree", "dead tree"]
        for i in range(len(treeNames)):
            if treeNames[i] == "none":
                continue
            path = f"assets/tree/tree{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.TreesList.append(pygame.transform.scale(img, (self.TILE_SIZE * 2, self.TILE_SIZE * 3)))
            self.Blocks.EveryBlock[(treeNames[i])] = self.TreesList[-1]

    def load_lake(self):
        self.LakeList = []
        lakeNames = ["lake0", "lake1", "lake2"]
        for i in range(len(lakeNames)):
            path = f"assets/water/lake{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.LakeList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(lakeNames[i])] = self.LakeList[-1]

    def load_items(self, SLOT_SIZE):
        self.ItemsList = []
        itemNames = ["sword", "pickaxe", "axe", "hoe", "wood", "stone", "iron_ingot", "iron_nugget", "emerald"]
        for i in range(len(itemNames)):
            path = f"assets/item/{itemNames[i]}.png"
            img = pygame.image.load(path).convert_alpha()
            self.ItemsList.append(pygame.transform.scale(img, (SLOT_SIZE*0.7, SLOT_SIZE*0.7)))
            self.Blocks.EveryBlock[(itemNames[i])] = self.ItemsList[-1]

    def load_cursor(self):
        img = pygame.image.load("assets/cursor.png").convert_alpha()
        cursorWidth = img.get_width()
        cursorHeight = img.get_height()
        self.CURSOR_SIZE_FACTOR = 2
        self.cursor = pygame.transform.scale(img,(cursorWidth * self.CURSOR_SIZE_FACTOR,
                                                          cursorHeight * self.CURSOR_SIZE_FACTOR))
        self.Objects.EveryObject["cursor"] = self.cursor

    def load_heart(self):
        img = pygame.image.load("assets/heart.png").convert_alpha()
        self.heart = pygame.transform.scale(img,(75,75))
        self.Objects.EveryObject["heart"] = self.heart

    def load_hotbar(self, inventoryRatio):
        self.HotbarList = []
        hotbarNames = ["hotbar_slot", "selected_hotbar_slot"]
        for i in range(len(hotbarNames)):
            path = f"assets/{hotbarNames[i]}.png"
            img = pygame.image.load(path).convert_alpha()
            self.HotbarList.append(pygame.transform.scale(img, (26*inventoryRatio, 26*inventoryRatio)))
            self.Objects.EveryObject[(hotbarNames[i])] = self.HotbarList[-1]



class Block:
    def __init__(block):
        block.EveryBlock = {}


class Objects:
    def __init__(object):
        object.EveryObject = {}