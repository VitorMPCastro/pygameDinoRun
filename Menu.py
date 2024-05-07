import pygame

from pygameDinoRun.Game import Game
from pygameDinoRun.GameObjects.Player.Dinosaur import Dinosaur


class Menu:

    @staticmethod
    def setMenuText(death_count):
        if death_count == 0:
            text = Game.FONT.render("Press any Key to Start", True, (0, 0, 0))
        else:
            text = Game.FONT.render("Press any Key to Restart", True, (0, 0, 0))
            Menu.setScoreText()
        textRect = text.get_rect()
        textRect.center = (Game.SCREEN_WIDTH // 2, Game.SCREEN_HEIGHT // 2)
        Game.SCREEN.blit(text, textRect)

    @staticmethod
    def setScoreText():
        score = Game.FONT.render("Your Score: " + str(Game.POINTS), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (Game.SCREEN_WIDTH // 2, Game.SCREEN_HEIGHT // 2 + 50)
        Game.SCREEN.blit(score, scoreRect)

    @staticmethod
    def drawMenu(death_count):
        Game.SCREEN.fill((255, 255, 255))
        Menu.setMenuText(death_count)
        Game.SCREEN.blit(Dinosaur.RUNNING[0], (Game.SCREEN_WIDTH // 2 - 20, Game.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

    @staticmethod
    def menuEventLoop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                return True
        return False


    @staticmethod
    def menu(death_count):
        while True:
            Game.SCREEN.fill((255, 255, 255))
            Menu.drawMenu(death_count)
            Menu.menuEventLoop()
