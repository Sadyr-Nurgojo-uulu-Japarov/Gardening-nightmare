import pygame

class Assets:
    def __init__(self, TILE_SIZE=64):
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
        self.FarmlandList = []
        farmlandNames = ["farmland"]
        for i in range(len(farmlandNames)):
            if farmlandNames[i] == "none":
                continue
            path = f"assets/grassfarmland/grassfarmland{i}.png"
            img = pygame.image.load(path).convert_alpha()
            self.FarmlandList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(farmlandNames[i])] = self.FarmlandList[-1]

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

    def load_items(self):
        self.ItemsList = []
        itemNames = ["sword", "pickaxe", "axe", "hoe", "wood", "stone", "iron ingot", "iron nugget", "emerald"]
        for i in range(len(itemNames)):
            path = f"assets/item/{itemNames[i]}.png"
            img = pygame.image.load(path).convert_alpha()
            self.ItemsList.append(pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE)))
            self.Blocks.EveryBlock[(itemNames[i])] = self.ItemsList[-1]

    def load_cursor(self):
        img = pygame.image.load("assets/cursor.png").convert_alpha()
        cursorWidth = img.get_width()
        cursorHeight = img.get_height()
        self.CURSOR_SIZE_FACTOR = 2
        self.cursor = pygame.transform.scale(img,(cursorWidth * self.CURSOR_SIZE_FACTOR,
                                                          cursorHeight * self.CURSOR_SIZE_FACTOR))
        self.Objects.EveryObject["cursor"] = self.cursor



class Block:
    def __init__(block):
        block.EveryBlock = {}


class Objects:
    def __init__(object):
        object.EveryObject = {}