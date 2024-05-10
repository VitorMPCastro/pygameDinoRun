import pygame
from pygameDinoRun.GameEventHandler import GameEventHandler
from pygameDinoRun.GameObjects.Player.Angola import Angola
from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.GameObjects.Obstacles.CarroG import CarroG
from pygameDinoRun.GameObjects.Obstacles.CarroP import CarroP
from pygameDinoRun.GameObjects.Obstacles.Placa import Placa
from pygameDinoRun.GameObjects.Background.BackgroundScroller import Background


class GameRunner:

    @staticmethod
    def run():
        run = True
        clock = pygame.time.Clock()
        player = Angola()
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
                if player.angola_rect.colliderect(obstacle.rect):
                    pygame.time.delay(500)
                    death_count += 1
                    Menu.menu(death_count)

            background.move(Game.GAME_SPEED)

            cloud.draw()
            cloud.update(Game.GAME_SPEED)

            Game.score()

            clock.tick(30)
            pygame.display.update()
