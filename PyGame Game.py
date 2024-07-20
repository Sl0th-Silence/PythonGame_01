import pygame

pygame.init()

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
bg = pygame.image.load('hillandale.png')
char = pygame.image.load('F1.png')

clock = pygame.time.Clock()

#Making a char
x = 5
y = 520
width = 16
height = 16
walkCount = 0
left = False
right = False

isJump = False
jumpCount = 10

#Making Screen
screen_width = 800
screen_height = 600

#Set Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Game")

playerVelocity = 5

#WalkingAnimation

def redrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0, 0))
    if walkCount + 1 >= 24:
        walkCount = 0
    
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))
        
    
    pygame.display.update()
    

run = True
while run:
    clock.tick(24)

    key = pygame.key.get_pressed()
    #move
    if key[pygame.K_a] and x > playerVelocity:
        x -= playerVelocity
        left = True
        right = False
    elif key[pygame.K_d] and x < screen_width - width - playerVelocity:
        x += playerVelocity
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        #Jump
        if key[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    redrawGameWindow()
            
pygame.quit

