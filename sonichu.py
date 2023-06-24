#Sonichu
#AidenKrahn
#Started May 16

import pygame, random, csv, math

pygame.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sonichu: CWC's Love Quest")

clock = pygame.time.Clock()

ts = pygame.image.load('titscr.png')#titlescreen
music = pygame.mixer.music.load('august2021.wav')
pygame.mixer.music.set_volume(0.1)
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
        #self.stam = 120#stamina bar not needed
        self.vel = 15#
        self.jumpCount = 9.5#how high can he jump
        self.isJump = False#whether he is jumping
        self.facing = 1#what way is he facing
        self.spin = False
        self.walk = False#whether he's walking. never used
        self.walkCount = 0#walking animation cycling through the list
        self.jumpdraw = 0#jumping animation cycling through the list
        self.spin2 = False#spin was being used while jumping, and due to technical issues they wouldn't work as the same variable
        self.spinCount = 0#how long he's spinning for
        self.notSpin = 0#cooldown for not spinning
        self.canSpin = True#after notspin is done, he can spin again
        self.isHit = True # NOT SWEARING
        self.isHitting = False#this one, as well as the one abovce, would be used if I could collision with enemies and spikes. they would change if he was spinning or not
        self.maskWalk = pygame.mask.from_surface(f0)#getting a mask while walking. basically a collision outline, but I just used rect instead
        self.rect = f0.get_rect()#collision for player
        self.maskSpin = pygame.mask.from_surface(f10)#mask from spin. also collision outline, just used 
        self.health = 3
        self.onGround = True #whether he was on ground or not jumping
        self.neg = 1#what direction he's going while jumping
        
    def draw(self,win):
        self.rect.x = self.x#making sure rect and self are aligned
        self.rect.y = self.y
        self.x = self.rect.x
        self.y = self.rect.y
        if self.spin == True or self.spin2 == True: # which rect to use (they're the same anyways)
            self.rect = f10.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.rect = f0.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            
        pygame.draw.rect(win, (white), self.rect, 2)#draw rect for some reason
        if self.spin2 == True or self.canSpin == False:
            s.stamBar(win)#ig he's spinning or recovering after spinning, show stamina bar
        if self.facing == 1:#if facing right
            
            if self.isJump == False:#if not jumping
                
                if self.spin2 == False:#or spinning
                    
                    if self.walk == False:#or moving
                        win.blit(f1, (self.x, self.y))
                        
                    elif self.walk == True:#if he is walking
                        self.walkCount += 1
                        if self.walkCount >= 8:
                            self.walkCount = 0
                        win.blit(walkRight[int(self.walkCount / 2)], (self.x, self.y))
                        
                elif self.spin2 == True:#if he is spinning
                    self.walkCount += 1
                    if self.walkCount >= 4:
                        self.walkCount = 0
                        
                    win.blit(spinRight[int(self.walkCount)], (self.x, self.y))
                        
                
            elif self.isJump == True:#if he is jumping
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
                        
        elif self.facing == -1:#same as everything before but Left
            
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
        if self.y == 500:#if the charater is on the lowest level without being on the screen, he's on the ground
            self.onGround = True
        keys = pygame.key.get_pressed()#get pressed key
        if keys[pygame.K_RIGHT] == False or keys[pygame.K_LEFT] == False:
            brt.shmove = False#don't move the background if not moving
        
        if keys[pygame.K_DOWN]:#spinning
            if self.canSpin == True:#if able to spin
                self.spin2 = True#start spinning
                self.notSpin = 40#start the counter for the cooldown
                self.vel = 30#change vel
                brt.vel = 30#make sure background can keep up
                self.spinCount = 0#the spin will try to get back up
                self.canSpin = False#can't spin again while spinning
                
            else:
                pass
            
        if self.spin2 == True:    
            
            if self.spinCount <= 20:#once at 20, spinning while stop
                self.spinCount += 1
                self.isHitting = True
                
            if self.spinCount >= 20:#stop spinning, set stuff back to normal
                self.spin2 = False
                self.vel = 10
                brt.vel = 10
                self.notSpin = 50
                
        if self.notSpin >= 0:#if counter is counting down, can't spin
            self.canSpin = False
            self.notSpin -= 1
            
        else:
            self.canSpin = True
            
            
        if keys[pygame.K_RIGHT]:# move right
            self.facing = 1
            if self.x < 350:#if between two points on the screen, you are allowed to move
                self.x += self.vel * self.facing
                brt.shmove = False
                
            else:#the background and everything moves around you instead of you
                brt.scroll(win,self)
                if self.x < 350 and key[pygame.K_RIGHT]:
                    brt.shmove = True
            self.walk = True
            
        elif keys[pygame.K_LEFT]:# same thing but left
            self.facing = -1
            if self.x > 30:
                self.x += self.vel * self.facing
                brt.shmove = False
                
            else:
                brt.scroll(win,self)#small bug here: if at the beginning of the level and you walk left, everything other than the background will scroll right
                if self.x > 30 and keys[pygame.K_LEFT]:
                    brt.shmove = True
            self.walk = True
            
        elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
            self.walk = False#default pose
            
        if not(self.isJump):#if not jumping and press up
                
            if keys[pygame.K_UP] and self.onGround == True:
                self.isJump = True
                self.spin2 = False
                self.vel = 10
                brt.vel = 10
                self.onGround = False
                
        else:
            if self.jumpCount >= 0:#going up
                self.neg = 1
            if self.jumpCount < 0:#going down
                self.neg = -1
                
            self.y -= (self.jumpCount ** 2) * 0.7 * self.neg#HYPOTHETICALLY, the code will allow him to go down once the jumpcount goes past 0. This doesn't work. 
            self.jumpCount -= 1# jumpcount goes down
            
            if self.jumpCount >= 9.5:#terminal velocity
                self.jumpCount = 9.5
            
#             if self.y == 500 - self.jumpCount:
#                 self.isJump = False
#                 self.jumpCount = 9.5
                
            if self.onGround == True:#if touching ground, stop jumping
                self.isJump = False
                self.jumpCount = 9.5
                
    def stamBar(self,win):#just drawing stamina bar based on whether spinning or cooling down
        if self.spin2 == True:
            pygame.draw.rect(win,green,pygame.Rect(s.x, s.y - 40, 120,20))
            pygame.draw.rect(win,red,pygame.Rect(s.x, s.y - 40, self.spinCount*5, 20))
            
        else:
            pygame.draw.rect(win, green, pygame.Rect(s.x, s.y - 40, 120,20))
            pygame.draw.rect(win, red, pygame.Rect(s.x,s.y-40,self.notSpin*2.4,20))
                
    def hit(self,win,gus):# trying to get collision to work, part 2. virtually the same thing I have in a later section. neither work.
        
        if self.rect.colliderect(gus.rect.x, gus.rect.y, gus.width, gus.height):#if colliding in the x direction(with thing in list)
            self.vel = 0#stop moving. doesn't work
            
        else:
            pass
            #self.vel = 15
            
        if self.rect.colliderect(gus.rect.x, gus.rect.y + (self.jumpCount ** 2) * 0.7 * self.neg, gus.width, gus.height):#if colliding in the y direction
            if self.neg == 1:#if going up and hits something
                self.neg = -1#start going down
                self.jumpCount = 0
                self.onGround = False
                
            if self.neg == -1:#if going down and hits something
                self.onGround = True#is on ground
                self.jumpCount = 9.5
            self.onGround = True
    
    def hitting(self,win):
        pass

        
#normal enemy
class Troll(object):
    def __init__(self,x,y,width,height,xlimit):
        self.x = x#where he is 
        self.xo = x#where he was originally (you'll see)
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.facing  = 1
        self.xlimit = xlimit#how far he can move before turning around
        self.frame = 0
        self.alive = True
        self.mask = pygame.mask.from_surface(t0)
        self.rect = t0.get_rect()
        
    def draw(self,win):#animation
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
        if brt.shmove == True:#if background is moving, he'll move with it, closer to s
            if s.facing == 1:
                self.x = self.x - brt.vel
                self.xo = self.xo - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
                self.xo = self.xo + brt.vel
            
        if self.facing == 1:#moving back and forth
            self.x += self.vel
            if self.x > self.xo + self.xlimit:
                self.facing = -1
            
        if self.facing == -1:
            self.x -= self.vel
            if self.x < self.xo - self.xlimit:
                self.facing = 1
                
    def col(self,win):#didn't even try
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(win, (white), self.rect, 2)
        
            
class Background(object):
    def __init__(self,x):
        self.x = x
        self.y = 0
        self.vel = 10
        self.shmove = False
        self.xo = x
        
        
    def scroll(self,win,s):#the background will move when the player reaches a specific x coordinate
        if self.x <= -7600:
            self.x = -7599
            brt.shmove = False
        if self.x >= 0:
            self.x = -1
            brt.shmove = False
            
        if self.xo == x:
            self.x = -1
            brt.schmove = False
            
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
            
        
class Plat(object):#bricks & floor
    def __init__(self,x,y):
        self.x = x
        self.rect = brickimg.get_rect()
        self.y = y
        self.width = 100
        self.height = 100
        
    def schmoovin(self,win):#move with background
        if brt.shmove == True:
            if s.facing == 1:
                self.x = self.x - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
                
    def col(self,win):#same thing as what is above in player
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(win, (white), self.rect, 2)
        
        if self.rect.colliderect(s.rect.x, s.rect.y, s.width, s.height):
            s.vel = 0
            
        else:
            s.vel = 15
            
        if self.rect.colliderect(s.rect.x, s.rect.y + (s.jumpCount ** 2) * 0.7 * s.neg, s.width, s.height):
            if s.neg == 1:
                s.neg = -1
                s.jumpCount = 9.5
                
            if s.neg == -1:
                s.onGround = True
            s.onGround = True
    
class Hurt(object):#spikes. same properties as brick pretty much
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.rect = bluespikeimg.get_rect()
        
    def schmoovin(self,win):
        if brt.shmove == True:
            if s.facing == 1:
                self.x = self.x - brt.vel
                
            if s.facing == -1:
                self.x = self.x + brt.vel
                
    def col(self,win):
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(win, (white), self.rect, 2)
    
class Drink(object):
    def __init__(self,x,y,width,height):
        pass
    
class World():
    def __init__(self):
        pass
        
    def process(self,data):#process data from csv file, adding objects based on where it's located in the list of lists
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    if tile == 1:
                        floor = Plat(x * 100, (y * 100) - 50)
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
    image = pygame.Surface((width,height)).convert_alpha()#makes a black canvas
    image.blit(sheet, (0,0), (0,(frame * height), 22,(height * frame) + width))#puts image on canvas, based on coord of frame
    image = pygame.transform.scale(image,(big,big))#scale image to 100 * 100 pixels
    image.set_colorkey(color)#take away black canvas
    return image



def titlescreen(run,bg):
    while run == True:#title screen
        clock.tick(60)
        pygame.time.delay(30)
        win.blit(bg,(0,0))
        
        #s.draw(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bg = bg1#move onto next level
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
        win.blit(bg,(brt.x,brt.y))#draw background
        for pm in pmList:#do things for everything in world
            pm.draw(win)
            pm.schmoovin(win)
            pm.col(win)
            
        for brick in brickList:#''
            win.blit(brickimg, (brick.x,brick.y))
            brick.schmoovin(win)
            brick.col(win)
            s.hit(win,brick)
            
        for spike in spikeList:#''
            win.blit(bluespikeimg, (spike.x,spike.y))
            spike.schmoovin(win)
            spike.col(win)
            
        for floor in floorList:#''
#             floor.schmoovin(win)
            floor.col(win)#for some reason collide works better with bricks than with the floor, despite being the same code
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        s.draw(win)
        s.move(win)
                
        pygame.display.update()
                
    
rows = 7
cols = 84

worldData = []
for row in range(rows):
    r = [1] * cols#create a list of lists full of "blank spaces"
    worldData.append(r)
    
#load in level data
#print(worldData)
with open(f'slvldata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            worldData[x][y] = int(tile)#create list of lists from csv file
            
#print(worldData)
world = World()
#lines 553-618 are loading in images
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

#brickimg = get_image(brickimg,0,22,22,black,100)
# bluespikeimg = get_image(bluespikeimg,0,32,32,black,100)
brickimg = pygame.transform.scale(brickimg, (100,100))
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
#create player instance
s = Player(250,500,100,100)
pmList = []
brickList = []
spikeList = []
drinkList = []
floorList = []

world.process(worldData)
titlescreen(run,ts)
    
pygame.quit()


#i think the worst part about giving up now i knowing that i'm so close, that i'm one step from figuring out why my player goes through blocks or gets just above them
#before stopping. why my floor isn't there even though it's there in the list. I feel like I'm one small breakthrough away from solving everything, but nobody can tell me what it is.
