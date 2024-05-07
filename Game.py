import pygame


class Game:
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 1100
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    OBSTACLES = []
    POINTS = 0
    GAME_SPEED = 20
    FONT = pygame.font.Font('freesansbold.ttf', 20)

    @staticmethod
    def score():
        Game.POINTS += 1
        if Game.POINTS % 100 == 0:
            Game.GAME_SPEED += 1

        text = Game.FONT.render("Points: " + str(Game.POINTS), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        Game.SCREEN.blit(text, textRect)
