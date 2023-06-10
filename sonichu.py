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
        #self.stam = 120#stamina bar
        self.vel = 15#
        self.jumpCount = 9.5#how high can he jump
        self.isJump = False#whether he is jumping
        self.facing = 1#what way is he facing
        self.spin = False
        self.walk = False
        self.walkCount = 0
        self.jumpdraw = 0
        self.spin2 = False
        self.spinCount = 0
        self.notSpin = 0
        self.canSpin = True
        self.isHit = True # NOT SWEARING
        self.isHitting = False
        self.maskWalk = pygame.mask.from_surface(f0)
        self.rectWalk = f0.get_rect()
        
    def draw(self,win):
        if self.spin2 == False:
            pygame.draw.rect(win, red, (s.x, s.y, 100,100))
        if self.spin2 == True or self.canSpin == False:
            s.stamBar(win)
        if self.facing == 1:
            
            if self.isJump == False:
                
                if self.spin2 == False:
                    
                    if self.walk == False:
                        win.blit(f1, (self.x, self.y))
                        
                    elif self.walk == True:
                        self.walkCount += 1
                        if self.walkCount >= 8:
                            self.walkCount = 0
                        win.blit(walkRight[int(self.walkCount / 2)], (self.x, self.y))
                        
                elif self.spin2 == True:
                    self.walkCount += 1
                    if self.walkCount >= 4:
                        self.walkCount = 0
                        
                    win.blit(spinRight[int(self.walkCount)], (self.x, self.y))
                        
                
            elif self.isJump == True:
                self.jumpdraw += 1
                if self.jumpdraw >= 4:
                    self.jumpdraw = 0
                    self.spin = True
                    
                if self.spin == False:
                    win.blit(jumpRight[int(self.jumpdraw / 2)], (self.x,self.y))
                    
                elif self.spin == True:
                    win.blit(spinRight[int(self.jumpdraw)], (self.x,self.y))
                    if self.y == 500:
                        self.spin = False
                        
        elif self.facing == -1:
            
            if self.isJump == False:
                
                if self.spin2 == False:
                    
                    if self.walk == False:
                        win.blit(f12, (self.x, self.y))
                        
                    elif self.walk == True:
                        self.walkCount += 1
                        if self.walkCount >= 8:
                            self.walkCount = 0
                        win.blit(walkLeft[int(self.walkCount / 2)], (self.x, self.y))
                        
                elif self.spin2 == True:
                    
                    self.walkCount += 1
                    if self.walkCount >= 4:
                        self.walkCount = 0
                        
                    win.blit(spinLeft[int(self.walkCount)], (self.x, self.y))
                    
                
            elif self.isJump == True:
                self.jumpdraw += 1
                self.spin2 = False
                if self.jumpdraw >= 4:
                    self.jumpdraw = 0
                    self.spin = True
                    
                if self.spin == False:
                    win.blit(jumpLeft[int(self.jumpdraw / 2)], (self.x,self.y))
                    
                elif self.spin == True:
                    win.blit(spinLeft[int(self.jumpdraw)], (self.x,self.y))
                    if self.y == 500:
                        self.spin = False
    
    def move(self,win):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_DOWN]:
            if self.canSpin == True:
                self.spin2 = True
                self.notSpin = 40
                self.vel = 30
                brt.vel = 30
                self.spinCount = 0
                self.canSpin = False
                
            else:
                pass
            
        if self.spin2 == True:    
            
            if self.spinCount <= 20:
                self.spinCount += 1 
                
            if self.spinCount >= 20:
                self.spin2 = False
                self.vel = 10
                brt.vel = 10
                self.notSpin = 50
                
        if self.notSpin >= 0:
            self.canSpin = False
            self.notSpin -= 1
            
        else:
            self.canSpin = True
            
            
        if keys[pygame.K_RIGHT]:
            self.facing = 1
            if self.x <= 350:
                self.x += self.vel * self.facing
                
            else:
                brt.scroll(win,self)
            self.walk = True
            
        elif keys[pygame.K_LEFT]:
            self.facing = -1
            if self.x >= 30:
                self.x += self.vel * self.facing
                
            else:
                brt.scroll(win,self)
            self.walk = True
            
        elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
            self.walk = False
            
        if not(self.isJump):
                
            if keys[pygame.K_UP]:
                self.isJump = True
                self.spin2 = False
                self.vel = 10
                brt.vel = 10
                
        else:
            if self.jumpCount >= -9.5:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.7 * neg
                self.jumpCount -= 1
                
            else:
                self.isJump = False
                self.jumpCount = 9.5
                
    def stamBar(self,win):
        if self.spin2 == True:
            pygame.draw.rect(win,green,pygame.Rect(s.x, s.y - 40, 120,20))
            pygame.draw.rect(win,red,pygame.Rect(s.x, s.y - 40, self.spinCount*5, 20))
            
        else:
            pygame.draw.rect(win, green, pygame.Rect(s.x, s.y - 40, 120,20))
            pygame.draw.rect(win, red, pygame.Rect(s.x,s.y-40,self.notSpin*2.4,20))
                
    def hit(self,win):
        pass
    
    def hitting(self,win):
        pass

        
#normal enemy
class Troll(object):
    def __init__(self,x,y,width,height,xlimit):
        self.x = x
        self.xo = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.facing  = 1
        self.xlimit = xlimit
        self.frame = 0
        self.alive = True
        
    def draw(self,win):
        if self.facing == 1:
            win.blit(tWalkRight[int(self.frame/2)], (self.x, self.y))
            self.frame += 1
            if self.frame >= 12:
                self.frame = 0
            
        if self.facing == -1:
            win.blit(tWalkLeft[int(self.frame/2)], (self.x,self.y))
            self.frame += 1
            if self.frame >= 12:
                self.frame = 0
                
    def schmoovin(self,win):
        self.x = brt.x - self.x
        self.xo = brt.x - self.xo
        if self.facing == 1:
            self.x += self.vel
            if self.x > self.xo + self.xlimit:
                self.facing = -1
            
        if self.facing == -1:
            self.x -= self.vel
            if self.x < self.xo - self.xlimit:
                self.facing = 1
        
            
class Background(object):
    def __init__(self,x):
        self.x = x
        self.y = 0
        self.vel = 10
        
        
    def scroll(self,win,s):
        if self.x <= -7600:
            self.x = -7599
        if self.x >= 0:
            self.x = -1
        else:
            if s.facing == 1:
                self.x -= self.vel
                
            else:
                self.x += self.vel
            
class Boss(object):
    def __init__(self,x,y,width,height):
        pass
    
class Bullet(object):
    def __init__(self,x,y,width,height):
        pass
            
        
class Level(object):
    def __init__(self):
        pass

def get_image(sheet,frame,width,height, color, big):#taking an image from a sprite sheet
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), (0,(frame * height), 22,(height * frame) + width))
    image = pygame.transform.scale(image,(big,big))
    image.set_colorkey(color)
    return image



def titlescreen(run,bg,f):
    while run == True:
        clock.tick(60)
        pygame.time.delay(30)
        win.blit(bg,(0,0))
        
        #s.draw(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bg = bg1
            lv1(run,bg)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        #s.move(win)
                
        pygame.display.update()
        
    
def lv1(run,bg):
    while run == True:
        clock.tick(60)
        pygame.time.delay(40)
        win.blit(bg,(brt.x,brt.y))
        s.draw(win)
        t.draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        s.move(win)
        t.schmoovin(win)
                
        pygame.display.update()
                
            
ts = pygame.transform.scale(ts, (800,600))
run = True
Srun = pygame.image.load('Sr.png').convert_alpha()
Srun = pygame.transform.scale(Srun,(22,242))
Sleft = pygame.transform.flip(Srun, True,False)

Pright = pygame.image.load('Pm.png').convert_alpha()
Pright = pygame.transform.scale(Pright, (22,22*6))
Pleft = pygame.transform.flip(Pright,True,False).convert_alpha()
bg1 = pygame.image.load('bg.jpg').convert_alpha()
brt = Background(0)
            
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

t0 = get_image(Pright,0,22,22,black,100)
t1 = get_image(Pright,1,22,22,black,100)
t2 = get_image(Pright,2,22,22,black,100)
t3 = get_image(Pright,3,22,22,black,100)
t4 = get_image(Pright,4,22,22,black,100)
t5 = get_image(Pright,5,22,22,black,100)

t6 = get_image(Pleft,0,22,22,black,100)
t7 = get_image(Pleft,1,22,22,black,100)
t8 = get_image(Pleft,2,22,22,black,100)
t9 = get_image(Pleft,3,22,22,black,100)
t10 = get_image(Pleft,4,22,22,black,100)
t11 = get_image(Pleft,5,22,22,black,100)

walkRight = [f0,f1,f2,f3]
walkLeft = [f11,f12,f13,f14]
jumpRight = [f5,f6]
jumpLeft = [f16,f17]
spinRight = [f7,f8,f9,f10]
spinLeft = [f18,f19,f20,f21]

tWalkRight = [t0,t1,t2,t3,t4,t5]
tWalkLeft = [t6,t7,t8,t9,t10,t11]

s = Player(250,500,100,100)
t = Troll(300,500,100,100,100)

titlescreen(run,ts,f15)
    
pygame.quit()


