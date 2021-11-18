from nlc_dino_runner.components.obstacles.powerups.power_up import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

    def move(self, game_speed, moving):
        self.rect.x += game_speed + 5

        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -100
            moving.hammer_moving = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
