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
