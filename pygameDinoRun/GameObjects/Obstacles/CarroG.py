import pygame
import os
import random

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.Game import Game

CARRO_G = [pygame.image.load(os.path.join("Assets/Car", "CarG1.png")),
           pygame.image.load(os.path.join("Assets/Car", "CarG2.png")),
           pygame.image.load(os.path.join("Assets/Car", "CarG3.png"))]


class CarroG(Obstacle):

    def __init__(self):
        self.type = random.randint(0, 2)
        super().__init__(CARRO_G, self.type)
        self.rect.y = 310

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)


CarroG.register()
