import pygame

class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("ufo.png")
        self.playerX = 100
        self.playerY = 450
        self.playerX_change = 0

        self.bulletImg = pygame.image.load("bullet.png")
        self.bulletX = 0
        self.bulletY = 480
        self.bulletY_change = 5
        self.bullet_state = "ready"

    def fire_bullet(self):
        self.bullet_state = "fire"

    def make_move_or_shoot(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -1
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 1
            if event.key == pygame.K_SPACE:
                if self.bullet_state == "ready":
                    self.fire_bullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.playerX_change = 0
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 0

        self.playerX = self.playerX + self.playerX_change

        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 768:
            self.playerX = 768

        if self.bullet_state == "fire":
            self.bulletX = self.playerX
            screen.blit(self.bulletImg, (self.bulletX, self.bulletY))
            self.bulletY -= self.bulletY_change

        if self.bulletY <= 0:
            self.bulletY = 480
            self.bullet_state = "ready"

    def draw_player(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))


