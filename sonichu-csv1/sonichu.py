#Sonichu
#AidenKrahn
#Started May 16

import pygame, random, csv

pygame.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sonichu: CWC's Love Quest")

clock = pygame.time.Clock()

ts = pygame.image.load('titscr.png')#titlescreen

music = pygame.mixer.music.load('august2021.wav')
pygame.mixer.music.play(-1)
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
        self.maskSpin = pygame.mask.from_surface(f10)
        self.rectSpin = f10.get_rect()
        self.health = 3
        self.inAir = False
        
    def draw(self,win):
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
                    self.isHitting = False
                    win.blit(jumpRight[int(self.jumpdraw / 2)], (self.x,self.y))
                    
                elif self.spin == True:
                    self.isHitting = True
                    win.blit(spinRight[int(self.jumpdraw)], (self.x,self.y))
                    if self.y == 500:
                        self.spin = False
                        
        elif self.facing == -1:
            
            if self.isJump == False:
                
                if self.spin2 == False:
                    self.isHitting = False
                    
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
        if self.y == 500:
            self.onGround = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] == False or keys[pygame.K_LEFT] == False:
            brt.shmove = False
        
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
                self.isHitting = True
                
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
            if self.x < 350:
                self.x += self.vel * self.facing
                brt.shmove = False
                
            else:
                brt.scroll(win,self)
                if self.x < 350 and key[pygame.K_RIGHT]:
                    brt.shmove = True
            self.walk = True
            
        elif keys[pygame.K_LEFT]:
            self.facing = -1
            if self.x > 30:
                self.x += self.vel * self.facing
                brt.shmove = False
                
            else:
                brt.scroll(win,self)
                if self.x > 30 and keys[pygame.K_LEFT]:
                    brt.shmove = True
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
        self.mask = pygame.mask.from_surface(t0)
        self.rect = t0.get_rect()
        
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
        if brt.shmove == True:
            if s.facing == 1:
                self.x = self.x - brt.vel
                self.xo = self.xo - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
                self.xo = self.xo + brt.vel
            
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
        self.shmove = False
        
        
    def scroll(self,win,s):
        if self.x <= -7600:
            self.x = -7599
            brt.shmove = False
        if self.x >= 0:
            self.x = -1
            brt.shmove = False
        else:
            if s.facing == 1:
                self.x -= self.vel
                brt.shmove = True
                
            else:
                self.x += self.vel
                brt.shmove = True
            
class Boss(object):
    def __init__(self,x,y,width,height):
        pass
    
class Bullet(object):
    def __init__(self,x,y,width,height):
        pass
            
        
class Plat(object):
    def __init__(self,x,y):
        self.x = x
        
        self.y = y
        self.width = 100
        self.height = 100
        self.mask = pygame.mask.from_surface(brickimg)
        
    def schmoovin(self,win):
        if brt.shmove == True:
            if s.facing == 1:
                self.x = self.x - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
    
class Hurt(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.mask = pygame.mask.from_surface(bluespikeimg)
        
    def schmoovin(self,win):
        if brt.shmove == True:
            if s.facing == 1:
                self.x = self.x - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
    
class Drink(object):
    def __init__(self,x,y,width,height):
        pass
    
class World():
    def __init__(self):
        pass
        
    def process(self,data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    if tile == 1:
                        floor = Plat(x * 100, y * 100)
                        floorList.append(floor)
                        
                    if tile == 2:
                        brick = Plat(x * 100, y * 100)
                        brickList.append(brick)
                        
                    if tile == 3:
                        pm = Troll(x * 100,y * 100,100,100,30)
                        pmList.append(pm)
                    if tile == 4:
                        bs = Hurt(x * 100, y * 100)
                        spikeList.append(bs)
                    if tile == 5:
                        #boss
                        pass
                    if tile == 6:
                        #drink
                        pass
                    

def get_image(sheet,frame,width,height, color, big):#taking an image from a sprite sheet
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), (0,(frame * height), 22,(height * frame) + width))
    image = pygame.transform.scale(image,(big,big))
    image.set_colorkey(color)
    return image



def titlescreen(run,bg):
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
        for pm in pmList:
            pm.draw(win)
            pm.schmoovin(win)
            
        for brick in brickList:
            win.blit(brickimg, (brick.x,brick.y))
            brick.schmoovin(win)
            
        for spike in spikeList:
            win.blit(bluespikeimg, (spike.x,spike.y))
            spike.schmoovin(win)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        s.move(win)
                
        pygame.display.update()
                
    
tileSize = 100
rows = 7
cols = 84

worldData = []
for row in range(rows):
    r = [1] * cols
    worldData.append(r)
    
#load in level data
print(worldData)
with open(f'slvldata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            worldData[x][y] = int(tile)
            
print(worldData)
world = World()

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
brickimg = pygame.image.load('brick.png').convert_alpha()
bluespikeimg = pygame.image.load('bluespike.png').convert_alpha()

brickimg = get_image(brickimg,0,22,22,black,100)
# bluespikeimg = get_image(bluespikeimg,0,32,32,black,100)
bluespikeimg = pygame.transform.scale(bluespikeimg, (100,100))
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
pmList = []
brickList = []
spikeList = []
drinkList = []
floorList = []

world.process(worldData)
titlescreen(run,ts)
    
pygame.quit()
