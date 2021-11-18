import random
import pygame
from nlc_dino_runner.components.obstacles.powerups.shield import Shield
from nlc_dino_runner.components.obstacles.powerups.hammer import Hammer
from nlc_dino_runner.utils.constants import SHIELD_TYPE, HAMMERS, HAMMER_TYPE, DEFAULT_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.shield_type = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))
        self.hammer = Hammer()
        self.hammer_moving = False
        self.hammers_available = HAMMERS

    def reset_power_ups(self, points):
        self.power_ups = []
        self.power_ups_manager = [Shield, Hammer]
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating powerup")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                random.shuffle(self.option_numbers)
                if self.option_numbers[0] <= 5:
                    self.power_ups.append(Shield())
                    self.shield_type.append(self.power_ups[0])
                else:
                    self.power_ups.append(Hammer())
        return self.power_ups, self.shield_type

    def update(self, points, game_speed, player, user_input):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(15, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield = True
                    player.show_text = True
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)

                else:
                    power_up.start_time = pygame.time.get_ticks()
                    player.hammer = True
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                    if self.hammers_available == 0:
                        self.hammers_available = 3
                        player = DEFAULT_TYPE
                        player.hammer = False

        if player.hammer and user_input[pygame.K_SPACE] and not self.hammer_moving:
            self.hammers_available -= 1
            self.hammer_moving = True
            self.hammer.rect.x = player.dino_rect.x
            self.hammer.rect.y = player.dino_rect.y
        if self.hammers_available == 0:
            player.type = DEFAULT_TYPE
            player.hammer = False

        if self.hammer_moving:
            self.hammer.move(game_speed, self)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        if self.hammer_moving:
            self.hammer.draw(screen)
