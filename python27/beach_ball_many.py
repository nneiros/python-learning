import pygame,sys
from random import *
class Beach_Balls(pygame.sprite.Sprite):
      def __init__(self,image_file,location,speed):
          pygame.sprite.Sprite.__init__(self)
          self.image=pygame.image.load(img_file)
          self.rect=self.image.get_rect()
          self.rect.left,self.rect.top=location
          #seld.rect.speed=speed

     
size=width,height=340,340
screen=pygame.display.set_mode(size)
img_file="beach_ball.png"
balls=[]
for i in range(3):
   for j in range(3):
       location=[j*100+10,i*100+10]
       speed=[choice([-2,2]),choice([-2,2])]
       ball=Beach_Balls(img_file,location,speed)
       balls.append(ball)

for ball in balls:
   screen.blit(ball.image,ball,rect)
pygame.display.flip()

while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
        
