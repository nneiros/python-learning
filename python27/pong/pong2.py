# Ping versjon 0.1
#Player 1=W,S kai Player2= Pano,Kato Belakia
import pygame, sys, math, random
from pygame.locals import *

pygame.init()

# Definerer farger
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def main():

    # Initialisere settings og klokke
    clock = pygame.time.Clock()
    settings = {};
    settings['show_framerate'] = False
    settings['framerate'] = 60
    settings['screen_size'] = settings['width'], settings['height'] = (640, 480)
    settings['currentframerate'] = settings['framerate']

    settings['paused'] = False
    settings['players'] = pygame.sprite.Group()
    settings['balls'] = pygame.sprite.Group()
    settings['player1'] = Player('Spiller 1', [50, settings['height'] /2], settings['screen_size'], WHITE)
    settings['player1_score'] = 0
    settings['player1_up'] = K_w
    settings['player1_down'] = K_s
    settings['player2'] = Player('Spiller 2', [settings['width']-50, settings['height'] /2], settings['screen_size'], WHITE)
    settings['player2_score'] = 0
    settings['player2_up'] = K_UP
    settings['player2_down'] = K_DOWN
    settings['score_changed'] = True
    settings['players'].add(settings['player1'], settings['player2'])
    settings['balls'].add(Ball([settings['width']/2, settings['height']/2], settings['screen_size']))

    font = pygame.font.Font(None, 30) #font = pygame.font.Font('arial', 30)
    fpstext = font.render("FPS: "+ str(settings['currentframerate']), 1, WHITE)
    fpstextpos = fpstext.get_rect()

    # Initialiserer skjerm
    screen = pygame.display.set_mode(settings['screen_size'], 32)
    pygame.display.set_caption("Ping v0.1")
    random.seed()
    pygame.mouse.set_visible(False)

    # Gameloop
    while True:
        start_tick = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_f:
                    settings['show_framerate'] = not settings['show_framerate']
                elif event.key == K_p:
                    settings['paused'] = not settings['paused']
                elif event.key == K_a:
                    settings['balls'].add(settings['balls'].sprites()[0].maketwin())
                elif event.key == K_1:
                    settings['player1'].modify_size(2)
                elif event.key == K_2:
                    settings['player2'].modify_size(0.5)
                elif event.key == K_3:
                    settings['player1'].modify_speed(10)
                elif event.key == K_4:
                    settings['player2'].modify_speed(1)
                elif event.key == K_5:
                    settings['balls'].sprites()[0].set_speed(2)
                elif event.key == K_6:
                    settings['balls'].sprites()[0].set_speed(10)
                elif event.key == K_q:
                    settings['player1'].modify_speed(5)
                    settings['player2'].modify_speed(5)
                    settings['player1'].modify_size(1)
                    settings['player2'].modify_size(1)
                    settings['balls'].sprites()[0].set_speed(5)

        if not settings['paused']:
            # Checking input
            keys = pygame.key.get_pressed()
            if keys[settings['player1_up']]:
                settings['player1'].moveup()
            if keys[settings['player1_down']]:
                settings['player1'].movedown()
            if keys[settings['player2_up']]:
                settings['player2'].moveup()
            if keys[settings['player2_down']]:
                settings['player2'].movedown()

            # Moving ball(s)
            settings['balls'].update()
            # Fjerner baller som gaar utenfor skjermen
            for ball in settings['balls'].sprites():
                if ball.rect.left < 0:
                    settings['player2_score'] += 1
                    settings['balls'].remove(ball)
                    settings['score_changed'] = True
                elif ball.rect.right > settings['width']:
                    settings['player1_score'] += 1
                    settings['balls'].remove(ball)
                    settings['score_changed'] = True
            # Legger til en ny ball om det finnes 0 baller paa brettet
            if not bool(settings['balls']):
                settings['balls'].add(Ball([settings['width']/2, settings['height']/2], settings['screen_size']))

            # Sjekker kollisjoner
            ball_player_collisions = pygame.sprite.groupcollide(settings['balls'] ,settings['players'], False, False)
            for ball in ball_player_collisions.iterkeys():
                ball.crash(ball_player_collisions[ball])
        else:
            pausetext = font.render("Pause", 1, WHITE)
            pausetext_rect = pausetext.get_rect()
            pausetext_rect = pausetext_rect.move((settings['width'] - pausetext_rect.width) / 2 , (settings['height'] - pausetext_rect.height) / 2)

        # Tegner opp skjermbildet
        screen.fill(BLACK)
        if settings['show_framerate']:
            fpstext = font.render("FPS: "+ str(int(clock.get_fps())), 1, WHITE)
            screen.blit(fpstext, fpstextpos)

        if settings['paused']:
            screen.blit(pausetext, pausetext_rect)

        if settings['score_changed']:
            p1text = font.render("Player 1: "+ str(settings['player1_score']) + " poeng", 1, WHITE)
            p1text_rect = p1text.get_rect()
            p1text_rect = p1text_rect.move(5, settings['height'] - p1text_rect.height - 5)
            p2text = font.render("Player 2: "+ str(settings['player2_score']) + " poeng", 1, WHITE)
            p2text_rect = p2text.get_rect()
            p2text_rect = p2text_rect.move(settings['width'] - p2text_rect.width - 5, settings['height'] - p2text_rect.height - 5)
            settings['score_changed'] = False

        screen.blit(p1text, p1text_rect)
        screen.blit(p2text, p2text_rect)
        settings['players'].draw(screen)
        settings['balls'].draw(screen)
        for ball in settings['balls']:
            ball.render(screen)
        pygame.display.update()

        # Adjusting framerate
        time = (1000/settings['framerate']) - pygame.time.get_ticks() + start_tick
        clock.tick()
        if time > 0:
            pygame.time.wait(time)

class Ball(pygame.sprite.Sprite):

    def __init__(self, position, screensize, color = WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.speed = 5
        if random.random() < 0.5:
            temp = -1.0
        else:
            temp = 1.0
        if random.random() < 0.5:
            temp2 = -1.0
        else:
            temp2 = 1.0
        self.vector = Vector2(temp*random.randint(10,30), temp2*random.randint(10,20))
        self.vector.normalize()
        self.screensize = screensize

        self.image = pygame.Surface((10,10))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, self.color, (5,5), 5)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0], position[1])

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self, players):
        self.vector = Vector2(-self.vector.x, self.vector.y)
        for player in players:
            left = abs(player.rect.left - self.rect.right)
            right = abs(player.rect.right - self.rect.left)
            top = abs(player.rect.top - self.rect.bottom)
            bottom = abs(player.rect.bottom - self.rect.top)
            if left == min(left, right, top, bottom):
                self.vector = Vector2(-abs(self.vector.x), self.vector.y)
            elif right == min(left, right, top, bottom):
                self.vector = Vector2(abs(self.vector.x), self.vector.y)
            elif top == min(left, right, top, bottom):
                self.vector = Vector2(self.vector.x, -abs(self.vector.y))
            elif bottom == min(left, right, top, bottom):
                self.vector = Vector2(self.vector.x, abs(self.vector.y))

    def update(self):
        self.rect = self.rect.move(self.vector.x * self.speed, self.vector.y * self.speed)
        if self.rect.top < 0 or self.rect.bottom > self.screensize[1]:
            self.vector = Vector2(self.vector.x, -self.vector.y)

    def set_speed(self, new_speed):
        self.speed = new_speed

    def maketwin(self):
        twin = Ball([self.rect.left, self.rect.top], self.screensize)
        twin.vector = Vector2(self.vector.x, -self.vector.y)
        twin.speed = self.speed
        return twin

class World(object):

    def __init__(self, p1, p2):
        self.players = (p1, p2)

class Player(pygame.sprite.Sprite):

    def __init__(self, name, position, screensize, color = (255,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.name = name
        self.size = [20,100]
        self.color = color
        self.screensize = screensize

        self.image = pygame.Surface((20,100))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0]-self.size[0]/2, position[1]-self.size[1]/2)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def moveup(self):
        if (self.rect.top > 0):
            self.rect = self.rect.move(0,-self.speed)

    def movedown(self):
        if (self.rect.bottom < self.screensize[1]):
            self.rect = self.rect.move(0,self.speed)

    def modify_speed(self, speed):
        self.speed = speed

    def modify_size(self, size):
        self.rect = Rect(self.rect.left, self.rect.top-((self.size[1]*size-self.rect.height)/2), self.size[0], self.size[1]*size)
        self.image = pygame.transform.scale(self.image, (self.size[0], int(size*self.size[1])))

class Vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, s):
        return Vector2(self.x * s, self.y * s)

    def __div__(self, s):
        return Vector2(self.x / s, self.y / s)

    def __str__(self):
        return "Vector2 (%s, %s)"%(self.x, self.y)

    def length(self):
        return math.sqrt((self.x**2 + self.y**2))

    def normalize(self):
        l = self.length()
        self.x /= l
        self.y /= l

    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0]-P1[0], P2[1]-P1[1])

if __name__ == '__main__': main()
#<!-- Page not cached by WP Super Cache. No closing HTML tag. Check your theme. -->
