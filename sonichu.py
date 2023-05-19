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
    def __init__(self,x,y,width,height,fr):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = []
        self.stam = 10#stamina bar
        self.vel = 10#
        self.acc = 0#speed up and slow down gradually instead of 0 - 100
        self.jump = 10#how high can he jump
        self.isJump = 0#whether he is jumping
        self.facing = 1#what way is he facing
        self.fr = fr
        
    def jump(self,win,x,y,width,height):
        pass
    
    def punch(self,win,hitbox):
        pass
    
    def run(self,win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.facing = 1
            self.x += self.vel * self.facing
            
        elif keys[pygame.K_LEFT]:
            self.facing = -1
            self.x += self.vel * self.facing
                
        
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
        win.blit(f,(s.x,s.y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        s.run(win)
                
        pygame.display.update()
                
            
            
f0 = get_image(Srun,0,22,22, black,100)
s = Player(250,250,100,100,f0)
            
titlescreen(run,ts,s.fr)
    
pygame.quit()
