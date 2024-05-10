import pygame
import os

from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.Game import Game

PLACA = [pygame.image.load(os.path.join("Assets/Placa", "Placa.png"))]

POSTE = pygame.image.load(os.path.join("Assets/Placa", "Poste.png"))

class Poste:
    def __init__(self):
        self.image = POSTE
        self.rect = self.image.get_rect()
        self.rect.x = Game.SCREEN_WIDTH
        self.rect.y = 260

    def update(self, game_speed):
        self.rect.x -= game_speed

    def draw(self):
        Game.SCREEN.blit(self.image, self.rect)

class Placa(Obstacle):
    def __init__(self, size=(60, 60)):
        self.type = 0
        super().__init__(PLACA, self.type)
        self.rect.y = 230
        self.poste = Poste()
        self.image = [pygame.transform.scale(img, size) for img in self.image]

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.poste.update(game_speed)

    def draw(self):
        self.poste.draw()
        Game.SCREEN.blit(self.image[0], self.rect)

    @classmethod
    def register(cls):
        Obstacle.OBSTACLE_TYPES.append(cls)

Placa.register()
