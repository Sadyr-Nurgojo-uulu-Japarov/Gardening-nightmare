class TileClass:
    def __init__(tile,x,y,screen):
        tile.x = x
        tile.y = y
        tile.size = screen.get_rect()[2]
        tile.is_owned = False
        tile.unowned_type = None
        tile.plant = None

    def is_walked_on(tile,player):
        return tile.x < player.x < tile.x + 50 and tile.y < player.y < tile.y + 50
        
