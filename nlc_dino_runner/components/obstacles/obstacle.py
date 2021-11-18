from nlc_dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, image, index):
        self.image = image
        self.index = index
        self.rect = (self.image[self.index].get_rect())
        self.rect.x = SCREEN_WIDTH
        self.time = 0
        self.game_speed = 15

    def update(self, obstacles):
        self.rect.x -= 10
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        return self.game_speed

    def draw(self, screen):
        screen.blit(self.image[self.index], self.rect)
