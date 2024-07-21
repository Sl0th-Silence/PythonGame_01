import pygame

pygame.init()

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
bg = pygame.image.load('hillandale.png')
char = pygame.image.load('F1.png')

clock = pygame.time.Clock()

#Making a char

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.playerVelocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def draw(self, screen):

        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x,self.y))

#Making Screen
screen_width = 800
screen_height = 600

#Set Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Game")

#WalkingAnimation

def redrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0, 0))
    man.draw(screen)
    pygame.display.update()
    
man = player(5, 500, 32, 32)

#mainLoop
run = True
while run:
    clock.tick(24)

    key = pygame.key.get_pressed()
    #move
    if key[pygame.K_a] and man.x > man.playerVelocity:
        man.x -= man.playerVelocity
        man.left = True
        man.right = False
    elif key[pygame.K_d] and man.x < screen_width - man.width - man.playerVelocity:
        man.x += man.playerVelocity
        man.left = False
        man.right = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        #Jump
        if key[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    redrawGameWindow()
            
pygame.quit

