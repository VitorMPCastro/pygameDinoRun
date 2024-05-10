import pygame
import os
import random

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle

CARRO_P = [pygame.image.load(os.path.join("Assets/Car", "CarP1.png")),
           pygame.image.load(os.path.join("Assets/Car", "CarP2.png"))]


class CarroP(Obstacle):
    def __init__(self):
        self.type = random.randint(0, 1)
        super().__init__(CARRO_P, self.type)
        self.rect.y = 310

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)

CarroP.register()
