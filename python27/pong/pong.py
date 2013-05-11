# Pong #den leitourgei sosta h raketa tou computer
import random, pygame, sys
from pygame.locals import *

FPS = 300
WINWID = 640
WINHEI = 480

BROWN = (102, 51, 0)
LIGHTBLUE = (0, 204, 204)
GREEN = (0, 153, 0)
PADDLECOLOR = (255, 255, 255)
BALLCOLOR = PADDLECOLOR
BACKGROUNDCOLOR = (0, 0, 0)

def main():
    global FPSCLOCK, DISPLAYSURF
    SPEED = 1
    DIFF = 1.0 # AI paddle speed handicap
    ball_speed = 1
    AISIGHT = WINWID/6
    FONT = "Times New Roman"
    pygame.init()
    DEFAULTFONT = pygame.font.SysFont(FONT, 16)
    BIGGERFONT = pygame.font.SysFont(FONT, 32)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWID, WINHEI))
    DISPLAYSURF.fill(BACKGROUNDCOLOR)
    BACKGROUND = pygame.Rect(0, 0, WINWID, WINHEI)
    pygame.display.set_caption('Pong')
    paddleUP, paddleDOWN = False, False    
    ballpos = (WINWID/2, WINHEI/2)
    AIpoint, PLAYERpoint = 0, 0
    score = "Player:%2f || Computer:%2f" % (AIpoint, PLAYERpoint)
    paddle = WINHEI/2
    AIpaddle = paddle
    pygame.draw.rect(DISPLAYSURF, BACKGROUNDCOLOR, BACKGROUND)
    pygame.draw.line(DISPLAYSURF, PADDLECOLOR, (9, paddle-20), (9, paddle+20), 3)
    pygame.draw.line(DISPLAYSURF, PADDLECOLOR, (629, AIpaddle-20), (629, AIpaddle+20), 3)
    pygame.draw.circle(DISPLAYSURF, BALLCOLOR, ballpos, 5)
    slope, y_int = ballpath(None, ballpos[0], ballpos[1])
    while True:
        for event in pygame.event.get():
            direction = None
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w):
                    paddleUP = True
                elif (event.key == K_DOWN or event.key == K_s):
                    paddleDOWN = True
            elif event.type == KEYUP:
                if (event.key == K_UP or event.key == K_w):
                    paddleUP = False
                elif (event.key == K_DOWN or event.key == K_s):
                    paddleDOWN = False
        # move player paddle
        if paddleUP and paddle >= 20:
            paddle-=SPEED
        elif paddleDOWN and paddle <= 460:
            paddle+=SPEED
        # move AI paddle
        if ballpos[0] > (AISIGHT):
            if AIpaddle-20 < ballpos[1] and AIpaddle <= 460:
                AIpaddle+=SPEED/DIFF
            elif AIpaddle+20 > ballpos[1] and AIpaddle >= 20:
                AIpaddle-=SPEED/DIFF
        # move ball
        x = ballpos[0] + ball_speed
        y = (slope*x) + y_int
        ballpos = (x, y)
        # if it hits a paddle
        if 9 < ballpos[0] < 11:
            if paddle-20 < ballpos[1] < paddle+20:
                slope, y_int = ballpath(None, ballpos[0], ballpos[1])
                ball_speed*=-1
        elif 629 < ballpos[0] < 631:
            if AIpaddle-20 < ballpos[1] < AIpaddle+20:
                slope, y_int = ballpath(None, ballpos[0], ballpos[1])
                ball_speed*=-1
        # if it hits the top or bottom
        if WINHEI-5 > ballpos[1] or ballpos[1] < 5:
            slope, y_int = ballpath(slope, ballpos[0], ballpos[1])
        # if paddle misses ball
        if ballpos[0] < 5:
            AIpoint+=1
            score = "Player:%2f || Computer:%2f" % (PLAYERpoint, AIpoint)
            ballpos = (WINWID/2, WINHEI/2)
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 100), pygame.Rect(0, 0, 640, 480))
            DISPLAYSURF.blit(BIGGERFONT.render("Point: Computer", 1, PADDLECOLOR), (WINWID/3, WINHEI/3))
            paddle, AIpaddle = WINWID/2, WINWID/2
            for i in range(5):
                FPSCLOCK.tick(FPS)
        elif ballpos[0] > 635 and AIpaddle-20 < ballpos[1] < AIpaddle+20:
            PLAYERpoint+=1
            score = "Player:%2f || Computer:%2f" % (PLAYERpoint, AIpoint)
            ballpos = (WINWID/2, WINHEI/2)
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 100), pygame.Rect(0, 0, 640, 480))
            DISPLAYSURF.blit(BIGGERFONT.render("Point: Player", 1, PADDLECOLOR), (WINWID/3, WINHEI/3))
            for i in range(5):
                FPSCLOCK.tick(FPS)


        pygame.draw.rect(DISPLAYSURF, BACKGROUNDCOLOR, BACKGROUND)
        pygame.draw.line(DISPLAYSURF, PADDLECOLOR, (9, paddle-20), (9, paddle+20), 3)
        pygame.draw.line(DISPLAYSURF, PADDLECOLOR, (629, AIpaddle-20), (629, AIpaddle+20), 3)
        pygame.draw.circle(DISPLAYSURF, BALLCOLOR, ballpos, 5)
        DISPLAYSURF.blit(DEFAULTFONT.render(score, 1, PADDLECOLOR), (WINWID/3, 20))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def ballpath(old_slope, ball_x, ball_y):
    if old_slope == None:
        slope = int(random.random() * 2)
    else:
        slope = old_slope * -1
    y_int = ball_y - (slope * ball_x)
    return slope, y_int

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()
