import pygame
from player import Player
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player = Player()
enemy = Enemy()

score = 0
font = pygame.font.Font("freesansbold.ttf", 30)
textX = 10
textY = 10

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    if bulletX >= enemyX - 32:
        if bulletX <= enemyX + 32:
            if bulletY <= enemyY + 32:
                return True
    else:
        return False

def win():
    print("\nCONGRATULATIONS!\nYou have successfully completed your mission")
    print("Here is your trophy reward!")
    trophy = open("trophy.txt","r")
    print(trophy.read())
    trophy.close()
    exit()

running = True

while running == True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            player.make_move_or_shoot(event, screen)

    enemy.move()
    player.make_move_or_shoot(event, screen)

    collision = isCollision(enemy.enemyX, enemy.enemyY, player.bulletX, player.bulletY)
    if collision:
        score += 1
        enemy.set_position()

    if score == 25:
        win()

    player.draw_player(screen)
    enemy.draw_enemy(screen)
    show_score(textX, textY)
    pygame.display.update()