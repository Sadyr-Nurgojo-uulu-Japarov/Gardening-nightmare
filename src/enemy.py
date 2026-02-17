import pygame


class EnemyClass:

    def __init__(enemy, x, y, target):
        enemy.x = x
        enemy.y = y
        enemy.target = target  # (animal or player or plant)
    
    def update(enemy):
        # Move towards the target
        if enemy.x < enemy.target.x:
            enemy.x += 1
        elif enemy.x > enemy.target.x:
            enemy.x -= 1
        if enemy.y < enemy.target.y:
            enemy.y += 1
        elif enemy.y > enemy.target.y:
            enemy.y -= 1

    def draw(enemy, screen):
        pygame.draw.rect(screen, (255, 0, 0), (enemy.x, enemy.y, 20, 20))