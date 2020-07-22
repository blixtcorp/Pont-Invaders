import pygame
import random
import math
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

#music
mixer.music.load("pontmusicgachiturbo.mp3")
#mixer.sound("BL_BL_BL_bladlast.wav")
#mixer.music.load("blahst_more_burst.mp3")
#mixer.music.load("fuckingcumming.mp3")
#mixer.music.load("no_pot_but_pump.mp3")
#mixer.music.load("zarohh.mp3")
#mixer.music.load("Our_daddy_told_us_not_to_be_ashamed.mp3")
mixer.music.play(-1)

#creating the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Pont game on")
icon = pygame.image.load("kkomrade.png")
pygame.display.set_icon(icon)

#player icon
player_icon = pygame.image.load("pontwithahat.png")
playerX = 370
playerY = 500

playerX_move = 0

#enemy
enemy_icon = pygame.image.load("pontwillslaythis.png")
enemyX = random.randint(3, 736)
enemyY = random.randint(20,70)
enemyY_change = 0.5

#bullet, ready = you cant see bullet, fire = bullet is moving
bullet_icon = pygame.image.load("pontbulletlaser (2).png")
bulletX = 370
bulletY = 423
bulletY_change = 4
bullet_state = "ready"

#background
backgroundImage = pygame.image.load("pontinvaderbackground.jpg")
backgroundX = 0
backgroundY = 0

#score
score_value = 0
potPlayed = 1
bladlastPlayed = 1

font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

gameOverFont = pygame.font.Font("freesansbold.ttf", 64)
gameOverScoreFont = pygame.font.Font("freesansbold.ttf", 48)

def showScore(x, y):
    score = font.render("Weebs warlorded: " + str(score_value), True, (0, 188, 255))
    screen.blit(score, (x, y))

def gameOverText():
    gameOverText = gameOverFont.render("YOU LOST LUL", True, (255, 10, 10))
    screen.blit(gameOverText, (155, 150))
    gameOverScore = gameOverScoreFont.render("Weebs slayed: " + str(score_value), True, (0,255,10))
    screen.blit(gameOverScore, (200, 250))

def player(x,y):
    screen.blit(player_icon,(x, y))

def background():
    screen.blit(backgroundImage,(backgroundX, backgroundY))

def enemy(x,y):
    screen.blit(enemy_icon, (x, y))

def bullet(x,y):
    screen.blit(bullet_icon, (x, y))

def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, ((x - 67), y + 10))

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    
    if distance < 25:
        return True
    else:
        return False

#game loop
game_running = True
while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move = -2
        
            if event.key == pygame.K_RIGHT:
                playerX_move = 2

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("jodwaybullet.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_move = 0

    screen.fill((37, 42, 47))

    background()

    playerX += playerX_move
    enemyY += enemyY_change

    if playerX <= 3:
        playerX = 3
    elif playerX >= 736:
        playerX = 736

    #if enemyY <= 0:
        #make game over

    if bulletY <= -110:
        bulletY = 423
        bullet_state = "ready"
    if bullet_state is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletY_change

    isCollision = collision(enemyX, enemyY, bulletX, bulletY)

    if isCollision:
        bulletY = 423
        bullet_state = "ready"
        score_value += 1
        enemyY_change += 0.05
        enemyX = random.randint(3, 736)
        enemyY = random.randint(2,70)

    if score_value == 5 and potPlayed == 1:
            scoreFiveSound = mixer.Sound("no_pot_but_pump.wav")
            scoreFiveSound.play()
            potPlayed = 0
    
    if score_value == 10 and bladlastPlayed == 1:
        scoreTenSound = mixer.Sound("BL_BL_BL_bladlast.wav")
        scoreTenSound.play()
        bladlastPlayed = 0

    #you lost
    if enemyY >= 440:
        enemyY = 3000

        gameOverText()
       

    player(playerX, playerY) #calls player thing for the pont
    enemy(enemyX, enemyY)
    showScore(textX, textY)
    
    pygame.display.update()
