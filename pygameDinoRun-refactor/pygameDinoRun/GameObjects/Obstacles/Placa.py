import pygame
import os

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.Game import Game

PLACA = [pygame.image.load(os.path.join("Assets/Placa", "Placa1.png")),
         pygame.image.load(os.path.join("Assets/Placa", "Placa2.png"))]


class Placa(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(PLACA, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self):
        if self.index >= 9:
            self.index = 0
        Game.SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)

Placa.register()
