import pygame

pygame.init()

win = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("My Game")

#Spielwelt
bg = pygame.image.load("BG.png")
floor = pygame.image.load("floor.png")

class cliff():
    def __init__(self, x, y, box):
        self.x = x
        self.y = y
        self.box = box

left_cliff = pygame.image.load("left_cliff.png")
right_cliff = pygame.image.load("right_cliff.png")

clock = pygame.time.Clock()

#Charakter

walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
             pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
             pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
             pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
            pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
            pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
            pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


def redrawGameWindow():

    #background
    win.blit(bg, (0,0))

    #floor
    win.blit(floor, (0,700))
    win.blit(floor, (100,700))
    win.blit(floor, (200,700))
    win.blit(floor, (300,700))
    win.blit(floor, (400,700))
    win.blit(floor, (500,700))
    win.blit(floor, (600,700))
    win.blit(floor, (700,700))
    win.blit(floor, (800,700))
    win.blit(floor, (900,700))

    #left cliff
    win.blit(left_cliff, (0,300))

    #right cliff
    win.blit(right_cliff, (900,400))

    #player
    hero.draw(win)

    pygame.display.update()



#Main Loop

hero = player(100, 645, 64, 64)
run = True

while run:

    clock.tick(33)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False
        hero.standing = False
    elif keys[pygame.K_RIGHT] and hero.x < 1000 - hero.vel - hero.width:
        hero.x += hero.vel
        hero.left = False
        hero.right = True
        hero.standing = False
    else:
        hero.standing = True
        hero.walkCount = 0
    if not (hero.isJump):
        if keys[pygame.K_UP]:
            hero.isJump = True
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -10:
            hero.y -= (hero.jumpCount * abs(hero.jumpCount))
            hero.jumpCount -= 1
        else:
            hero.jumpCount = 10
            hero.isJump = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()