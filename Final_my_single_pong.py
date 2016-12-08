#Bonus Game
#Single Player Pong
#Ishna Verma
#IT 210

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SPRINGGREEN = (0, 255, 127)
BLUE = (0, 0, 255)
PURPLE = (160, 32, 240)
pygame.init()

#setting the screen size
sizeOfWindow = (801, 600)
screen = pygame.display.set_mode(sizeOfWindow)
pygame.display.set_caption("{$InGle pL@YeR P0nG}")

xCor = 400
yCor = 581

xCorBall = 40
yCorBall = 40

xCorSpeed = 0
yCorSpeed = 0

xCorBallSpeed = 5
yCorBallSpeed = 5

points = 0

#for paddle and it's movement within the window size
def drawRect(screen, x, y):
    if x <= 0:
        x = 0
    if x >= 650:
        x = 650
    pygame.draw.rect(screen, BLACK, [x, y, 115, 20 ])

finished = False
timer = pygame.time.Clock()
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xCorSpeed = -6
            elif event.key == pygame.K_RIGHT:
                xCorSpeed = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xCorSpeed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yCorSpeed = 0
    screen.fill(SPRINGGREEN)
    xCor += xCorSpeed
    yCor += yCorSpeed

    xCorBall += xCorBallSpeed
    yCorBall += yCorBallSpeed

    #control of the ball
    if xCorBall < 0:
        xCorBall = 0
        xCorBallSpeed = xCorBallSpeed * -1
    elif xCorBall > 800:
        xCorBall = 800
        xCorBallSpeed = xCorBallSpeed * -1
    elif yCorBall < 0:
        yCorBall = 0
        yCorBallSpeed = yCorBallSpeed * -1
    elif xCorBall > xCor and xCorBall < xCor + 100 and yCorBall == 565: #565
        yCorBallSpeed = yCorBallSpeed * -1
        points = points + 1
    elif yCorBall > 600:
        yCorBallSpeed = yCorBallSpeed * -1
        points = 0
    pygame.draw.rect(screen, BLUE, [xCorBall, yCorBall, 25, 25])

    #the shape of the ball is a square
    drawRect(screen, xCor, yCor)

    #to display the points
    fontStyle = pygame.font.SysFont("Castellar", 30, False, False)
    text = fontStyle.render("Points = " + str(points), True, BLACK)
    screen.blit(text, [350, 80])

    pygame.display.flip()
    timer.tick(45)

pygame.quit()