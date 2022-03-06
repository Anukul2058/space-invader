import pygame
import random
import math
from pygame import mixer

# initialize pygame
pygame.init()
pygame.display.set_caption('Space Invader By ANUKUL ')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)
score_value = 0

# initialize font


# player image
player_img = pygame.transform.scale(pygame.image.load('player.png'), (100, 100))
player_X = 300
player_Y = 500
player_change = 0

# loading background image
bg = pygame.transform.scale(pygame.image.load('background.png'), (600, 600))


# player
def player(player_X, player_Y):
    screen.blit(player_img, (player_X, player_Y))


# creating enemy
enemy_image = []
enemy_X = []
enemy_Y = []
enemy_xchange = []
enemy_ychange = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemy_image.append(pygame.transform.scale(pygame.image.load('enemy.png'), (40, 40)))
    enemy_X.append( random.randint(0, 600))
    enemy_Y.append( random.randint(50, 150))
    enemy_xchange.append( 1.8)
    enemy_ychange.append(  10)

# loading bullets
bullet_image = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_ychange = 3
bullet_xchange = 0
bullet_state = "ready"

#creating gameover text
text = pygame.font.SysFont(None,100)


# enemy
def enemy(enemy_X, enemy_Y ,i):
    screen.blit(enemy_image[i], (enemy_X, enemy_Y))

def game_over_text():
    text_img = text.render('GAME OVER', True, (200, 0, 0))

    screen.blit(text_img,(100,100))


# bullet
def bullet(bullet_X, bullet_Y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (bullet_X + 30, bullet_Y + 20))

# def collisonIs(enemy_X, enemy_Y, player_X, player_Y,):
#
#     distance = math.sqrt(math.pow(enemy_X - player_X, 2)) + math.sqrt(math.pow(enemy_Y - player_Y, 2))
#     if distance < 50:
#         return True
#     else:
#         return False





def collison_between_bullet(enemy_X, enemy_Y, bullet_X, bullet_Y):
    distance2 = math.sqrt(math.pow(enemy_X - bullet_X, 2)) + math.sqrt(math.pow(enemy_Y - bullet_Y, 2))
    if distance2 < 24:
        return True
    else:
        return False


# create the screen
screen = pygame.display.set_mode((600, 600))

running = True

# game loop
while running:
    font = pygame.font.SysFont(None, 30)


    img = font.render(f'score:{score_value}', True, (0, 200, 0))
    screen.blit(bg, (0, 0))
    screen.blit(img, (30, 20))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1.8
            if event.key == pygame.K_RIGHT:
                player_change = 1.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet_X = player_X
                    bullet(bullet_X, bullet_Y)


    # movement of player
    player_X += player_change
    if player_X >= 568:
        player_change = 0
    if player_X <= 0:
        player_change = 0
    # movement of enemy
    for i in range(number_of_enemies):
        if enemy_Y[i] > 458:
            for j in range(number_of_enemies):

                enemy_Y[j] = 2000
            game_over_text()
            break





        enemy_X[i] += enemy_xchange[i]

        if enemy_X[i] <= 0:
            enemy_xchange[i] = 1.8
            enemy_Y[i] += enemy_ychange[i]
        if enemy_X[i] >= 568:
            enemy_xchange[i] = -1.8
            enemy_Y[i] += enemy_ychange[i]
        collison2 = collison_between_bullet(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if collison2:
            bullet_state = 'ready'
            bullet_Y = 500

            enemy_X[i] = random.randint(0, 600)
            enemy_Y[i] = random.randint(50, 150)
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            score_value += 1
        enemy(enemy_X[i], enemy_Y[i], i)
    # movement of bullet
    if bullet_state is 'fire':
        bullet(bullet_X, bullet_Y)

        bullet_Y -= bullet_ychange
    if bullet_Y <= 0:
        bullet_Y = 500
        bullet_state = "ready"






    player(player_X, player_Y)
    pygame.display.update()

