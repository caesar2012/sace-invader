import pygame
import random

class Enemy:
    def __init__(self):
        self.enemyImg = pygame.image.load("alien.png")
        self.enemyX = 450
        self.enemyY = 100
        self.enemyX_change = 0.3
        self.enemyY_change = 20

    def move(self):
        self.enemyX += self.enemyX_change

        if self.enemyX <= 0:
            self.enemyX_change = 0.3
            self.enemyY += self.enemyY_change
        elif self.enemyX >= 768:
            self.enemyX_change = -0.3
            self.enemyY += self.enemyY_change

    def set_position(self):
        self.enemyX = random.randint(20, 760)
        self.enemyY = random.randint(50, 150)

    def draw_enemy(self, screen):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))


