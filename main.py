
# TO DO
# Respawn dopo aver fatto punto
# Secondo giocatore
# Vittoria a X punti
# Bersaglio mobile

# Ostacoli



import pygame
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1500, 800))

# Title, icon and background
pygame.display.set_caption("FrenzyBoi")
icon = pygame.image.load('target.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')

# Background sound
mixer.music.load('music.mp3')
mixer.music.play(-1)    # -1 is to play the track on loop

# Player
player1Img = pygame.image.load('player1_downdx.png')
player1X = 200
player1Y = 200
player1X_change = 1        # regulate the movement speed
player1Y_change = 1
player1X_direction = 0.5
player1Y_direction = 0.5
player1_centerX = player1X - 8     # centerX corresponds to the center of the player_image.png, which is 16x16 pixels
player1_centerY = player1Y - 8
points_player1 = 0

# Target
targetImg = pygame.image.load('target.png')
targetX = 750
targetY = 400
target_centerX = targetX - 8     # imageX corresponds to the center of the target_image.png, which is 16x16 pixels
target_centerY = targetY - 8

# Score
score_player1 = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_scoreX = 10
text_scoreY = 10


def player1(x, y, direction_x, direction_y):       # manages the visualization of the player icon, giving an image and a set of coordinates

    if direction_x > 0 and direction_y > 0:
        playerImg = pygame.image.load('player1_downdx.png')
        screen.blit(playerImg, (x, y))
    if direction_x < 0 and direction_y < 0:
        playerImg = pygame.image.load('player1_upsx.png')
        screen.blit(playerImg, (x, y))
    if direction_x > 0 and direction_y < 0:
        playerImg = pygame.image.load('player1_updx.png')
        screen.blit(playerImg, (x, y))
    if direction_x < 0 and direction_y > 0:
        playerImg = pygame.image.load('player1_downsx.png')
        screen.blit(playerImg, (x, y))


def target(x, y):           # manages the visualization of the target icon
    screen.blit(targetImg, (x, y))


def turn_left(x, y):
    if x > 0 and y > 0:
        return 1, -1
    if x < 0 and y < 0:
        return -1, 1
    if x > 0 and y < 0:
        return -1, -1
    if x < 0 and y > 0:
        return 1, 1


def turn_right(x, y):
    if x > 0 and y > 0:
        return -1, 1
    if x < 0 and y < 0:
        return 1, -1
    if x > 0 and y < 0:
        return 1, 1
    if x < 0 and y > 0:
        return -1, -1


def score(x_player, y_player, x_target, y_target):
    if math.sqrt((math.pow(x_player - x_target, 2) + math.pow(y_player - y_target, 2))) < 50:
        score_sound = mixer.Sound('laser.wav')
        score_sound.play()
        return True


def show_score(x, y):
    score = font.render("SCORE : " + str(score_player1), True, (255, 255, 255))
    screen.blit(score, (x, y))


def border_collision(x, y, x_direction, y_direction, playerX_change, playerY_change):
    if x >= 1500 or x <= 0:
        return -x_direction, -y_direction, playerX_change+0.2, playerY_change+0.2
    if y >= 800 or y <= 0:
        return -x_direction, -y_direction, playerX_change+0.2, playerY_change+0.2
    else:
        return x_direction, y_direction, playerX_change, playerY_change


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    #screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if score(player1X, player1Y, targetX, targetY):
            score_player1 += 1
# Keyboard controls
        if pygame.KEYDOWN == event.type:
            if event.key == pygame.K_w:     # pressing 'w' turns right
                player1X_direction, player1Y_direction = turn_right(player1X_direction, player1Y_direction)
            if event.key == pygame.K_q:     # pressing 'q' turns left
                player1X_direction, player1Y_direction = turn_left(player1X_direction, player1Y_direction)

    player1X += player1X_change*player1X_direction     # player movement
    player1Y += player1Y_change*player1Y_direction
    player1_centerX = player1X - 8                     # player ICON movement, otherwise the player moves but the icon doesn't
    player1_centerY = player1Y - 8

    player1X_direction, player1Y_direction, player1X_change, player1Y_change = border_collision(player1X, player1Y, player1X_direction, player1Y_direction, player1X_change, player1Y_change)

    player1(player1_centerX, player1_centerY, player1X_direction, player1Y_direction)      # print the player icon, I used centerX and centerY so that it playerX and playerY corresponds to the center (?)
    target(target_centerX, target_centerY)      # print the target icon
    show_score(text_scoreX, text_scoreY)        # print the Player 1 score
    pygame.display.update()     # to actually see things changing in the screen
