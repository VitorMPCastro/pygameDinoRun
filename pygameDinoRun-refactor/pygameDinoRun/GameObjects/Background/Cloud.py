import pygame
import os
import random

from pygameDinoRun.Game import Game

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))


class Cloud:
    def __init__(self):
        self.x = Game.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = Game.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self):
        Game.SCREEN.blit(self.image, (self.x, self.y))
