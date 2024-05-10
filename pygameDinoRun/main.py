import pygame
import random

pygame.init()
from pygameDinoRun.Game import Game
from pygameDinoRun.GameEventHandler import GameEventHandler
from pygameDinoRun.GameObjects.Player.Angola import Angola
from pygameDinoRun.GameObjects.Obstacles.Obstacle import Obstacle
from pygameDinoRun.GameObjects.Obstacles.CarroG import CarroG
from pygameDinoRun.GameObjects.Obstacles.CarroP import CarroP
from pygameDinoRun.GameObjects.Obstacles.Placa import Placa
from pygameDinoRun.GameObjects.Background.BackgroundScroller import Background


def main():
    run = True
    clock = pygame.time.Clock()
    player = Angola()
    background = Background(Game.SCREEN)
    death_count = 0



    while run:
        GameEventHandler.gameEventLoop()
        userInput = pygame.key.get_pressed()

        Game.SCREEN.fill((255, 255, 255))
        background.move(Game.GAME_SPEED)
        player.draw(Game.SCREEN)
        player.update(userInput)

        Obstacle.spawnRandomObstacle()

        for obstacle in Game.OBSTACLES:
            obstacle.draw()
            obstacle.update(Game.GAME_SPEED, Game.OBSTACLES)
            if player.angola_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                death_count += 1
                menu(death_count)

        Game.score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    run = True
    while run:
        Game.SCREEN.fill((255, 255, 255))

        if death_count == 0:
            text = Game.FONT.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = Game.FONT.render("Press any Key to Restart", True, (0, 0, 0))
            score = Game.FONT.render("Your Score: " + str(Game.POINTS), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Game.SCREEN_WIDTH // 2, Game.SCREEN_HEIGHT // 2 + 50)
            Game.SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (Game.SCREEN_WIDTH // 2, Game.SCREEN_HEIGHT // 2)
        Game.SCREEN.blit(text, textRect)
        Game.SCREEN.blit(Angola.RUNNING[0], (Game.SCREEN_WIDTH // 2 - 20, Game.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)