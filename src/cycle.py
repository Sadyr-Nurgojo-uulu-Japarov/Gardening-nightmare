import pygame


class DayNightCycleClass:
    def __init__(self, SCREEN_WIDTH):
        self.dayLength = 10
        self.timer = 0
        self.borderX = SCREEN_WIDTH - 2*(SCREEN_WIDTH // 10)
        self.state = "day"
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.COLOR_DAY = (255, 191, 0) 
        self.COLOR_NIGHT = (40, 40, 150)

    def update(self, dividedTime):
        self.timer += dividedTime
        if self.timer >= self.dayLength:
            self.timer = 0
            self.state = "day" if self.state == "night" else "night"

    def draw(self, screen):
        pygame.draw.rect(screen,(50,50,50),(self.borderX,50,220,70))
        if self.state == "day":
            current_label = "DAY"
            bar_color = self.COLOR_DAY
        else:
            current_label = "NIGHT"
            bar_color = self.COLOR_NIGHT

        time_percent = self.timer / self.dayLength
        bar_width = int(200 * time_percent) 
        pygame.draw.rect(screen, bar_color, (self.borderX + 10, 60, bar_width, 50))
        text_surf = self.font.render(current_label, True, (255, 255, 255))
        screen.blit(text_surf, (self.borderX + 20, 70))