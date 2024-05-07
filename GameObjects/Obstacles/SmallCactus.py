import pygame
import os
import random

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]


class SmallCactus(Obstacle):
    def __init__(self):
        self.type = random.randint(0, 2)
        super().__init__(SMALL_CACTUS, self.type)
        self.rect.y = 325

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)

SmallCactus.register()
