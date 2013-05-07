import pygame, random
from pygame.locals import *
pygame.init()
random.seed()

screen = pygame.display.set_mode((400, 400))
#pygame.display.set_caption("Im learning to make pong in pygame!")

sprite_paddle = pygame.image.load("paddle.png")
sprite_ball = pygame.image.load("ball.png")

rect_paddle1 = sprite_paddle.get_rect()
rect_paddle2 = sprite_paddle.get_rect()
rect_ball = sprite_ball.get_rect()

rect_ball.left = 200 - 12.5
rect_ball.top = 200 - 12.5
rect_paddle1.left = 200 - 50
rect_paddle2.left = 200 - 50
rect_paddle1.top = 0
rect_paddle2.top = 400 - 25

hspeed = 0
vspeed = 0
while hspeed == 0:
    hspeed = random.randint(-1,1)
    hspeed = hspeed
while vspeed == 0:
    vspeed = random.randint(-1,1)
    vpseed = vspeed
print (hspeed,vspeed)

slower = 15

run = True
while run:
    
#GAME-LOGIC-----------
#handle input
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
 if (rect_paddle1.left > 0):
     rect_paddle1.left -= 1
     if keys[pygame.K_RIGHT]:
         if (rect_paddle1.left < 300):
             rect_paddle1.left += 1
             if keys[pygame.K_a]:
                 if (rect_paddle2.left > 0):
                     rect_paddle2.left -= 1
                     if keys[pygame.K_d]:
                         if (rect_paddle2.left < 300):
                             rect_paddle2.left += 1

slower -= 1
if slower == 0:
    slower = 15
    
#horizontal movement for ball
    if hspeed < 0:
        if (rect_ball.left + hspeed > 0):
            rect_ball.left += hspeed
        else:
            hspeed = -hspeed
            else:
                if (rect_ball.left + hspeed < 375):
                        rect_ball.left += hspeed
                        else:
                            hspeed = -hspeed

#vertical movement for ball
if vspeed < 0:
if (rect_ball.top + vspeed > 0):
rect_ball.top += vspeed
else:
rect_ball.left = 200 - 12.5
rect_ball.top = 200 - 12.5
else:
if (rect_ball.top + vspeed < 375):
rect_ball.top += vspeed
else:
rect_ball.left = 200 - 12.5
rect_ball.top = 200 - 12.5

#ball collision with paddle1
coll = False
if ((rect_ball.left >= rect_paddle1.left) and (rect_ball.left <= rect_paddle1.left + rect_paddle1.width) and (rect_ball.top >= rect_paddle1.top) and (rect_ball.top <= rect_paddle1.top + rect_paddle1.height)):
coll = True
elif ((rect_paddle1.left >= rect_ball.left) and (rect_paddle1.left <= rect_ball.left + rect_ball.width) and (rect_paddle1.top >= rect_ball.top) and (rect_paddle1.top <= rect_ball.top + rect_ball.height)):
coll = True

#ball collision with paddle2
if ((rect_ball.left >= rect_paddle2.left) and (rect_ball.left <= rect_paddle2.left + rect_paddle2.width) and (rect_ball.top + rect_ball.height >= rect_paddle2.top) and (rect_ball.top + rect_ball.height <= rect_paddle2.top + rect_paddle2.height)):
coll = True
elif ((rect_paddle2.left >= rect_ball.left) and (rect_paddle2.left <= rect_ball.left + rect_ball.width) and (rect_paddle2.top >= rect_ball.top) and (rect_paddle2.top <= rect_ball.top + rect_ball.height)):
coll = True

if coll:
if ((rect_ball.top < 200) and (vspeed < 0)):
vspeed = -vspeed
elif ((rect_ball.top > 200) and (vspeed > 0)):
vspeed = -vspeed

#game logic ends here

#DRAWING--------------
screen.fill((0,0,0))
#draw code goes here
screen.blit(sprite_ball,rect_ball)
screen.blit(sprite_paddle,rect_paddle1)
screen.blit(sprite_paddle,rect_paddle2)
#end of draw code
pygame.display.flip()

pygame.quit()
