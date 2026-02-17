import pygame

class EnemyClass:

    def __init__(enemy, x, y, target):
        enemy.x = x
        enemy.y = y
        enemy.speed = 2
        enemy.target = target  # (animal or player or plant)
    
    def update(enemy):
        # Move towards the player
        diff_x = enemy.x - enemy.target.x
        diff_y = enemy.y - enemy.target.y
        maxi = max(abs(diff_x),abs(diff_y))
        mini = min(abs(diff_x),abs(diff_y))
        ratio = maxi/mini
        if maxi == abs(diff_x):
            
            enemy.x += enemy.speed * ratio * -1 if diff_x > 0 else enemy.speed * ratio
            enemy.y += enemy.speed
        else:
            enemy.x += enemy.speed
            enemy.y += enemy.speed * ratio * -1 if diff_y > 0 else enemy.speed * ratio

    def draw(enemy, screen):
        pygame.draw.rect(screen, (255, 0, 0), [enemy.x, enemy.y, 20, 20])