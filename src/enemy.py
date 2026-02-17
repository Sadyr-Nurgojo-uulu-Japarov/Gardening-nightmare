import pygame

class EnemyClass:
    def __init__(enemy, x, y, target, terrain):
        enemy.x = x  
        enemy.y = y
        enemy.SPEED = 2 
        enemy.target = target
        enemy.terrain = terrain
    
    def update(enemy):
        target_world_x = enemy.terrain.x + (enemy.terrain.SCREEN_WIDTH // 2)
        target_world_y = enemy.terrain.y + (enemy.terrain.SCREEN_HEIGHT // 2)

        diff_x = target_world_x - enemy.x
        diff_y = target_world_y - enemy.y
        distance = (diff_x ** 2 + diff_y ** 2) ** 0.5
        
        if distance > 5:
            enemy.x += (diff_x / distance) * enemy.SPEED
            enemy.y += (diff_y / distance) * enemy.SPEED

    def draw(enemy, screen):
        draw_x = enemy.x - enemy.terrain.x
        draw_y = enemy.y - enemy.terrain.y
        pygame.draw.rect(screen, (255, 0, 0), [draw_x, draw_y, 20, 20])