import pygame,sys         #??????????????????????trexei mono me akinites mpales
from random import *
class Beach_Balls(pygame.sprite.Sprite):
      def __init__(self,image_file,location,speed):
          pygame.sprite.Sprite.__init__(self)
          self.image=pygame.image.load(image_file)
          self.rect=self.image.get_rect()
          self.rect.left,self.rect.top=location
          seld.rect.speed=speed
          
      def move(self):
           self.rect=self.rect.move(self.speed)
           if self.rect.left<0 or self.rect.left>width:
              self.speed[0]=-self.speed[0]
           if self.rect.top<0 or self.rect.top>height:
             self.speed[1]=-self.speed[1]
     

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
      screen.blit(ball.image,ball.rect)
pygame.display.flip()

while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
         pygame.time.delay(20)
         screen.fill([0,0,0])
         for ball in balls:
             ball.move()
             screen.blit(ball.image, ball.rect)
             pygame.display.flip()
