import pygame

pygame.init()

#Making Screen
screen_width = 800
screen_height = 600

#Set Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Game")

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
bg = pygame.image.load('hillandale.png')
char = pygame.image.load('F1.png')

clock = pygame.time.Clock()

#making enemy


class enemy(object):
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
   
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 2, self.y, 28, 40)
        
    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        
        if self.vel > 0:
            screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 2, self.y, 28, 40)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                
    def hit(self):
        print("Hit!")
       
    
    
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
        self.standing = True
        self.hitbox = (self.x + 2, self.y, 28, 40)
    
    def draw(self, screen):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:screen.blit(walkLeft[0], (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        self.hitbox = (self.x + 2, self.y, 28, 40)


# Projectile

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0, 0))
    man.draw(screen)
    enemy1.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    pygame.display.update()
    
man = player(5, 500, 32, 32)
enemy1 = enemy(100, 500, 32, 32, 450)

shootLoop = 0
bullets = []
#mainLoop
run = True
while run:
    clock.tick(24)
    key = pygame.key.get_pressed()
    
    #Shoot cooldown
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 8:
        shootLoop = 0
    
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy1.hitbox[1] + enemy1.hitbox[3] and bullet.y + bullet.radius > enemy1.hitbox[1]:
            if bullet.x + bullet.radius > enemy1.hitbox[0] and bullet.x - bullet.radius < enemy1.hitbox[0] + enemy1.hitbox[2]:
                enemy1.hit()
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    
    if man.left:
        facing = -1
    else:
        facing = 1
        
    if key[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), 6, (0,0,0), facing))
            shootLoop = 1
    
    #move
    if key[pygame.K_a] and man.x > man.playerVelocity:
        man.x -= man.playerVelocity
        man.left = True
        man.right = False
        man.standing = False
    elif key[pygame.K_d] and man.x < screen_width - man.width - man.playerVelocity:
        man.x += man.playerVelocity
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.walkCount = 0
        man.standing = True
        
        
    if not(man.isJump):
        #Jump
        if key[pygame.K_w]:
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

