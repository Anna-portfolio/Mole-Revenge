import pygame
from pygame import mixer
import math
from threading import Timer
import random

pygame.init()

screen = pygame.display.set_mode((540, 540))

background = pygame.image.load('meadow.png')

pygame.display.set_caption("Mole's Revenge")

icon = pygame.image.load('mole-icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('mole-player.png')
playerX = 80
playerY = 400
playerX_change = 0
playerY_change = 0

hammerImg = pygame.image.load('hammer.png')
hammerX = random.randint(55, 485)
hammerY = random.randint(75, 485)


def player(x, y):
    screen.blit(playerImg, (x, y))


def hammer(x, y):
    screen.blit(hammerImg, (x, y))


score_value = 0

font = pygame.font.Font('ArchitectsDaughter-Regular.ttf', 35)
scoreX = 10
scoreY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


counter = 10
font = pygame.font.Font('ArchitectsDaughter-Regular.ttf', 35)
timeX = 380
timeY = 10


def game_timer():
    global counter
    counter -= 1
    Timer(1, game_timer).start()


game_timer()


def show_time(x, y):
    time = font.render("Time: " + str(counter), True, (0, 0, 0))
    screen.blit(time, (x, y))


def is_collision(playerX, playerY, hammerX, hammerY):
    distance = math.sqrt((math.pow(playerX - hammerX, 2)) + (math.pow(playerY - hammerY, 2)))
    if distance < 45:
        return True
    else:
        return False


game_over_font = pygame.font.Font('ArchitectsDaughter-Regular.ttf', 70)
game_overX = 100
game_overY = 240


def game_over(x, y):
    game_over_text = game_over_font.render("TIME'S UP!", True, (0, 0, 0))
    screen.blit(game_over_text, (x, y))


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_UP:
                playerY_change = -2
            if event.key == pygame.K_DOWN:
                playerY_change = 2

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 5:
        playerX = 5
    if playerY <= 75:
        playerY = 75
    if playerX >= 480:
        playerX = 480
    if playerY >= 465:
        playerY = 465

    collision = is_collision(playerX, playerY, hammerX, hammerY)
    if collision:
        score_sound = mixer.Sound('score.wav')
        score_sound.play()
        score_value += 1
        hammerX = random.randint(55, 485)
        hammerY = random.randint(75, 485)

    if counter == 0:
        game_over(game_overX, game_overY)
        running = False
        playerX = 2000
        playerY = 2000
        hammerX = 2000
        hammerY = 2000

    player(playerX, playerY)
    hammer(hammerX, hammerY)
    show_score(scoreX, scoreY)
    show_time(timeX, timeY)

    pygame.display.update()
