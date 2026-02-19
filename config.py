import pygame

class AssetsClass:
    def __init__(self):
        self.


class Consts:
    def __init__(const, screen):
        const.SCREEN_WIDTH, const.SCREEN_HEIGHT = screen.get_size()
        const.TILE_SIZE = 64
        const.PLAYER_SPEED = 10
        const.PLAYER_SIZE = 40
        const.ENEMY_SPEED = 2
        const.CURSOR_SIZE_FACTOR = 2
        const.INVENTORY_SLOT_SIZE = screen.get_rect()[2] // 19
        const.HOTBAR_RATIO = const.INVENTORY_SLOT_SIZE / 26
