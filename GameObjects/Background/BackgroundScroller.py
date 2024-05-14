import pygame
import os

class Background:
    def __init__(self, screen):
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.SCREEN = screen
        self.BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

    def move(self, game_speed):
        image_width = self.BG.get_width()
        self.SCREEN.blit(self.BG, (self.x_pos_bg, self.y_pos_bg))
        self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= game_speed
