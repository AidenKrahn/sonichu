#Sonichu
#AidenKrahn
#Started May 16

import pygame, random, math

pygame.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sonichu: CWC's Love Quest")
clock = pygame.time.Clock()
ts = pygame.image.load('titscr.png')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,128,0)
purple = (153,0,153)



class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = []
        self.stam = 10
        self.vel = 10
        self.acc = 0
        self.jump = 10
        self.isJump = 0
        self.facing = 1
        
    def jump(self,win,x,y,width,height):
        pass
    
    def punch(self,win,hitbox):
        pass
        
    
class Troll(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
    
bg = pygame.transform.scale(ts, (800,600))
run = True
Srun = pygame.image.load('Sr.png').convert_alpha()

def get_image(sheet,frame,width,height, color):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame * width),0, 22,22))
    image = pygame.transform.scale(image,(100,100))
    image.set_colorkey(color)
    return image

frame0 = get_image(Srun,0,22,22, black)

while run == True:
    clock.tick(50)
    win.blit(bg,(0,0))
    
    win.blit(frame0, (250,250))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
            
    pygame.display.update()
            
    keys = pygame.key.get_pressed()
    
pygame.quit()


