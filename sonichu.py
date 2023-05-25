#Sonichu
#AidenKrahn
#Started May 16

import pygame, random

pygame.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sonichu: CWC's Love Quest")

clock = pygame.time.Clock()

ts = pygame.image.load('titscr.png')#titlescreen


#define rgb colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,128,0)
purple = (153,0,153)

#----classes----
#what human controls
class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = []
        self.stam = 10#stamina bar
        self.vel = 10#
        self.jumpCount = 9#how high can he jump
        self.isJump = False#whether he is jumping
        self.facing = 1#what way is he facing
        self.spin = False
        self.walk = False
        self.walkCount = 0
        
    def draw(self,win):
        if self.facing == 1:
            
            if self.isJump == False:
                
                if self.spin == False:
                    
                    if self.walk == False:
                        win.blit(f0, (self.x, self.y))
                        
                    elif self.walk == True:
                        win.blit(walkRight[self.walkCount//2], (self.x, self.y))
    
    def move(self,win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.facing = 1
            self.x += self.vel * self.facing
            self.run = True
            
        elif keys[pygame.K_LEFT]:
            self.facing = -1
            self.x += self.vel * self.facing
            self.run = True
            
        if not(self.isJump):
                
            if keys[pygame.K_UP]:
                self.isJump = True
                
        else:
            if self.jumpCount >= -9:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.7 * neg
                self.jumpCount -= 1
                
            else:
                self.isJump = False
                self.jumpCount = 9
                
        
#normal enemy
class Troll(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

ts = pygame.transform.scale(ts, (800,600))
run = True
Srun = pygame.image.load('Sr.png').convert_alpha()
Srun = pygame.transform.scale(Srun,(22,242))
Sleft = pygame.transform.flip(Srun, True,False)



def get_image(sheet,frame,width,height, color, big):#taking an image from a sprite sheet
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), (0,(frame * height), 22,(height * frame) + width))
    image = pygame.transform.scale(image,(big,big))
    image.set_colorkey(color)
    return image

def redraw():
    pass


def titlescreen(run,bg,f):
    while run == True:
        clock.tick(50)
        pygame.time.delay(30)
        win.blit(bg,(0,0))
        s.draw(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        s.move(win)
                
        pygame.display.update()
                
            
            
f0 = get_image(Srun,0,22,22, black,100)
f1 = get_image(Srun,1,22,22, black,100)
f2 = get_image(Srun,2,22,22, black,100)
f3 = get_image(Srun,3,22,22, black,100)
f4 = get_image(Srun,4,22,22, black,100)
f5 = get_image(Srun,5,22,22, black,100)
f6 = get_image(Srun,6,22,22, black,100)
f7 = get_image(Srun,7,22,22, black,100)
f8 = get_image(Srun,8,22,22, black,100)
f9 = get_image(Srun,9,22,22, black,100)
f10 = get_image(Srun,10,22,22, black,100)

f11 = get_image(Sleft,0,22,22,black,100)
f12 = get_image(Sleft,1,22,22,black,100)
f13 = get_image(Sleft,2,22,22,black,100)
f14 = get_image(Sleft,3,22,22,black,100)
f15 = get_image(Sleft,4,22,22,black,100)
f16 = get_image(Sleft,5,22,22,black,100)
f17 = get_image(Sleft,6,22,22,black,100)
f18 = get_image(Sleft,7,22,22,black,100)
f19 = get_image(Sleft,8,22,22,black,100)
f20 = get_image(Sleft,9,22,22,black,100)
f21 = get_image(Sleft,10,22,22,black,100)


walkRight = [f0,f1,f2,f3]
walkLeft = [f11,f12,f13,f14]
jumpRight = [f5,f6]
jumpLeft = [f16,f17]
spinRight = [f7,f8,f9,f10]
spinLeft = [f18,f19,f20,f21]

s = Player(250,250,100,100)
            
titlescreen(run,ts,f15)
    
pygame.quit()
