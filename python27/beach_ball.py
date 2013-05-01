import pygame,sys,random
from pygame.color import THECOLORS
pygame.init()
screen=pygame.display.set_mode([400, 220])
my_ball=pygame.image.load('beach_ball.png')
x=50
y=50
x_speed=5
y_speed=5

screen.blit(my_ball,[x,y])
pygame.display.flip()
while True:
           for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     sys.exit()

           pygame.time.delay(20)
           pygame.draw.rect(screen,THECOLORS['black'],[x,y,90,90],0)
           x=x+x_speed
           y=y+y_speed 
     #Aν χτυπήσουμε κάποιο άκρο του παραθύρου η κατεύθυνση αλλάζει
           if x>screen.get_width()-90 or x<0:
             x_speed=-x_speed
           if y>screen.get_height()-90 or y<0:
              y_speed=-y_speed
           #if x>screen.get_width():
            #  x=0
           screen.blit(my_ball,[x,y])
           pygame.display.flip()

