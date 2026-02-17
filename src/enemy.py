import pygame

class EnemyClass:

    def __init__(enemy, x, y, target):
        enemy.x = x
        enemy.y = y
        enemy.speed = 4.95
        enemy.target = target  # (animal or player or plant)
    
    def update(enemy):
        # Move towards the player
        diff_x = enemy.target.x - enemy.x
        diff_y = enemy.target.y - enemy.y

        distance = (diff_x ** 2 + diff_y ** 2) ** 0.5
        if distance != 0:
            enemy.x +=  diff_x / distance * enemy.speed
            enemy.y += diff_y / distance * enemy.speed

    def draw(enemy, screen):
        pygame.draw.rect(screen, (255, 0, 0), [enemy.x, enemy.y, 20, 20])