import pygame
import os
import random

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.Game import Game

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]


class LargeCactus(Obstacle):

    def __init__(self):
        self.type = random.randint(0, 2)
        super().__init__(LARGE_CACTUS, self.type)
        self.rect.y = 300

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)


LargeCactus.register()
