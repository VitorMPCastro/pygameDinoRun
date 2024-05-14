import pygame
import os
class Angola:
    X_POS = 80
    Y_POS = 330
    Y_POS_DUCK = 345
    JUMP_VEL = 9
    RUNNING = [pygame.image.load(os.path.join("Assets/Angola", "AngolaRun1.png")),
               pygame.image.load(os.path.join("Assets/Angola", "AngolaRun2.png"))]

    JUMPING = pygame.image.load(os.path.join("Assets/Angola", "AngolaJump.png"))

    DUCKING = [pygame.image.load(os.path.join("Assets/Angola", "AngolaDuck1.png")),
               pygame.image.load(os.path.join("Assets/Angola", "AngolaDuck2.png"))]

    def __init__(self):
        self.angola_duck = False
        self.angola_run = True
        self.angola_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.RUNNING[0]
        self.angola_rect = self.image.get_rect()
        self.angola_rect.x = self.X_POS
        self.angola_rect.y = self.Y_POS

    def update(self, userInput):
        if self.angola_duck:
            self.duck()
        if self.angola_run:
            self.run()
        if self.angola_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.angola_jump:
            self.angola_duck = False
            self.angola_run = False
            self.angola_jump = True
        elif userInput[pygame.K_DOWN] and not self.angola_jump:
            self.angola_duck = True
            self.angola_run = False
            self.angola_jump = False
        elif not (self.angola_jump or userInput[pygame.K_DOWN]):
            self.angola_duck = False
            self.angola_run = True
            self.angola_jump = False

    def duck(self):
        self.image = self.DUCKING[self.step_index // 5]
        self.angola_rect = self.image.get_rect()
        self.angola_rect.x = self.X_POS
        self.angola_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.RUNNING[self.step_index // 5]
        self.angola_rect = self.image.get_rect()
        self.angola_rect.x = self.X_POS
        self.angola_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.JUMPING
        if self.angola_jump:
            self.angola_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.angola_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.angola_rect.x, self.angola_rect.y))

    def die(self):
        return True