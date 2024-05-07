import pygame
from pygameDinoRun.GameEventHandler import GameEventHandler
from pygameDinoRun.GameObjects.Background.Cloud import Cloud
from pygameDinoRun.GameObjects.Player.Dinosaur import Dinosaur
from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.GameObjects.Obstacles.LargeCactus import LargeCactus
from pygameDinoRun.GameObjects.Obstacles.SmallCactus import SmallCactus
from pygameDinoRun.GameObjects.Obstacles.Bird import Bird
from pygameDinoRun.GameObjects.Background.BackgroundScroller import Background


class GameRunner:

    @staticmethod
    def run():
        run = True
        clock = pygame.time.Clock()
        player = Dinosaur()
        cloud = Cloud()
        background = Background(Game.SCREEN)
        death_count = 0

        while run:
            GameEventHandler.gameEventLoop()
            userInput = pygame.key.get_pressed()

            Game.SCREEN.fill((255, 255, 255))
            player.draw(Game.SCREEN)
            player.update(userInput)

            Obstacle.spawnRandomObstacle()

            for obstacle in Game.OBSTACLES:
                obstacle.draw()
                obstacle.update(Game.GAME_SPEED, Game.OBSTACLES)
                if player.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(500)
                    death_count += 1
                    Menu.menu(death_count)

            background.move(Game.GAME_SPEED)

            cloud.draw()
            cloud.update(Game.GAME_SPEED)

            Game.score()

            clock.tick(30)
            pygame.display.update()
