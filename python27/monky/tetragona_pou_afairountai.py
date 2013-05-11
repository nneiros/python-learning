import sys, pygame 
import random 
import math 
 
class Animal(pygame.sprite.Sprite): 
    global screen 
    global background 
    global resolution 
    global number_animals 
     
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self) 
        self.dx = 0 
        self.dy = 0 
        self.size = random.randint(10,25) 
        self.rect = pygame.Rect(random.randint(10,resolution[0]-self.size), random.randint(10,resolution[1]-self.size), self.size, self.size) 
        self.image = pygame.Surface([self.size, self.size]) 
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255))) 
        self.alive = True 
         
    def update(self): 
        x = random.randint(0,10)-5 
        y = random.randint(0,10)-5 
         
        if random.randint(1,100)%20 == 0 : self.dx = x 
        if random.randint(1,100)%20 == 0 : self.dy = y 
         
        self.rect.x += self.dx 
        self.rect.y += self.dy 
         
        if ((self.rect.y >= (resolution[1] - self.size)) or (self.rect.y <= self.size)): 
            self.rect.y -= self.dy 
        if ((self.rect.x >= resolution[0] - self.size) or (self.rect.x <= self.size)): 
            self.rect.x -= self.dx   
 
    def draw(self): 
        if self.alive == True:  
            sfBackground.blit(self.image, self.rect.topleft) 
 
def Animal_Eaten(sprite1,sprite2): 
    if sprite1 == sprite2: return False 
    return pygame.sprite.collide_rect(sprite1,sprite2) 
     
#Set up Screen 
pygame.init() 
resolution = (640,480) 
screen = pygame.display.set_mode(resolution) 
pygame.display.set_caption('Tutorial 7 -- Hunters') 
sfBackground = pygame.Surface(screen.get_size()) 
sfBackground = sfBackground.convert() 
sfBackground.fill((0,0,0)) 
 
            
#Add a timer to the game to control frame rates 
clock = pygame.time.Clock() 
 
 
number_animals = 100               
herd =[] 
for i in range(1,number_animals): 
    herd.append(Animal()) 
 
font = pygame.font.SysFont("comicsansms", 24) 
 
while number_animals > 0: 
    #Limit to 60 frames a second 
    clock.tick(30) 
 
    sfBackground.fill((0,0,0))     
    text = font.render("Number of Animals : %s" % (number_animals+1), True, (255,255,255)) 
 
    for i in herd: 
        i.update() 
 
    for i in range(0,len(herd)):          
        for j in range(i+1,len(herd)): 
            if  Animal_Eaten(herd[i],herd[j]): 
                if herd[i].size - herd[j].size > 0: 
                    herd[j].alive = False 
                else: 
                    herd[i].alive = False 
     
    for i in herd: 
        if i.alive == False:  
            herd.remove(i) 
     
    number_animals = len(herd) - 1 
 
    for i in herd: 
        i.draw() 
     
    for event in pygame.event.get(): 
        if (event.type == pygame.QUIT  or (event.type == pygame.KEYDOWN and event.key  == pygame.K_ESCAPE)): 
            sys.exit() 
  
    sfBackground.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))              
    screen.blit(sfBackground, (0,0))                    
    pygame.display.flip()
