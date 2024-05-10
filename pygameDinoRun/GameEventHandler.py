import pygame
import os
import random


class GameEventHandler:

    @staticmethod
    def gameEventLoop():
        for event in pygame.event.get():
            GameEventHandler.gameEventQuit(event)

    @staticmethod
    def gameEventQuit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    @staticmethod
    def gameEventPlayerCollide():
        pass
