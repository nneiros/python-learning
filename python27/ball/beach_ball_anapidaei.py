import os, sys
import pygame
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Avoid!")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

player = pygame.Rect(500, 300, 40, 40)
playerImage = pygame.Surface((40, 40))

enemy = pygame.Rect(300, 400, 20, 20)
enemyImage = pygame.Surface((20, 20))
enemyImage.fill((RED))

food = pygame.Rect(300, 500 , 20, 20)
foodImage = pygame.Surface((20, 20))
foodImage.fill((GREEN))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

class Score(pygame.sprite.Sprite):
    """A sprite for the score."""

    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.xy = xy  #save xy -- will center our rect on it when we change the score
        self.font = pygame.font.Font(None, 50)  # load the default font, size 50
        self.color = (255, 165, 0)         # our font color in rgb
        self.score = 0  # start at zero
        self.reRender() # generate the image

    def update(self):
        pass

    def add(self, points):
        """Adds the given number of points to the score."""
        self.score += points
        self.reRender()
        if player.colliderect(food):
            return add

    def reset(self):
        """Resets the scores to zero."""
        self.score = 0
        self.reRender()

    def reRender(self):
        """Updates the score. Renders a new image and re-centers at the initial coordinates."""
        self.image = self.font.render("%d"%(self.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.xy

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True

    windowSurface.fill(WHITE)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right +=MOVESPEED

    if player.colliderect(enemy):
        pygame.quit()
        sys.exit()

    windowSurface.blit(playerImage, player)
    windowSurface.blit(enemyImage, enemy)
    windowSurface.blit(foodImage, food)

    score = Score((75, 575))

    pygame.display.update()
    mainClock.tick(40)




# use pygame to bounce/move loaded image around the screen
import sys, pygame
pygame.init()
size = width, height = 320, 240
# this determines the move direction/speed in pixels
# speed[0] left or right
# speed[1] up or down
speed = [2, 2]
# color uses r, g, b tuple
black = 0, 0, 0
# white works better here
white = 255, 255, 255
# create the window
screen = pygame.display.set_mode(size)
# give the window a title
pygame.display.set_caption("watch the beach ball bounce")
# make sure the image file is in the working directory
# or give full path name
ball = pygame.image.load("ball.bmp")
# create rectangle object you can move
# it is used to put the image on
ballrect = ball.get_rect()
while True:
    for event in pygame.event.get():
        # window corner x will exit
        if event.type == pygame.QUIT:
            sys.exit()
    # move the rectangle object
    ballrect = ballrect.move(speed)
    # change direction if left or right boundry is reached
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # change direction if top or bottom boundry is reached
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    # clear the screen with white background
    screen.fill(white)
    # put the image on the rectangle object
    screen.blit(ball, ballrect)
    # update screen
    pygame.display.flip()
    # small time delay
    milliseconds = 20
    pygame.time.delay(milliseconds)
