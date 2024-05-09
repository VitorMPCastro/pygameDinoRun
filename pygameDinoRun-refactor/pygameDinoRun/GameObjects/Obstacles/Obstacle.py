import random

from pygameDinoRun.Game import Game


class Obstacle:
    OBSTACLE_TYPES = []
    def __init__(self, image, sprite_variant):
        self.image = image
        self.type = sprite_variant
        self.rect = self.image[self.type].get_rect()
        self.rect.x = Game.SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self):
        Game.SCREEN.blit(self.image[self.type], self.rect)

    @staticmethod
    def spawnRandomObstacle():
        if len(Game.OBSTACLES) == 0:
            obstacle = random.choice(Obstacle.OBSTACLE_TYPES)
            Game.OBSTACLES.append(obstacle())
