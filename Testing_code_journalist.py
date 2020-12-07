import pygame
import sys
import os
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40
ani = 4
ACC = 0.5
FRIC = -0.12
hbox, vbox = 20, 20 #This is for barriers, which we don't need anymore

world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (255, 255, 255)
ALPHA = (0, 255, 0)
steps = 6
lvl = 0
forwardx = 600
backwardx = 230

'''
Objects
'''
# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base_floor_1_resize3.png').convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Car(pygame.sprite.Sprite):

    def __init__(self, x, y, img,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('broken_car4.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        

#parts for the car
class Backdoor(pygame.sprite.Sprite):
    """
    spawn the backdoor
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('back_car_door2.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

class Headlights(pygame.sprite.Sprite):
    """
    spawn the headlights
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('headlights_2.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

class Hood(pygame.sprite.Sprite):
    """
    spawn the hood
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hood_of_car_1.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

class Wheels(pygame.sprite.Sprite):
    """
    spawn the wheels
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('wheels1.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

class Engine (pygame.sprite.Sprite):
    """
    spawn the engine
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('engine4.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def time(self):
        time = time

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 1
        self.score = 0
        self.is_jumping = True
        self.is_falling = True
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load('Smol_Survivor_1.png')
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            rect = pygame.Rect(300, 220, hbox, vbox)

        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
            
    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

        if self.movex > 6:
            self.movex = 6
        if self.movex < -6:  #This is so you can press and let go of the 
            self.movex = -6  #d or a key and stop moving

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def update(self):
        """
        Update sprite position
        """

        # moving left
        if self.movex < 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        elif self.movex > 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        

        # collisions
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list1, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list2, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list3, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list4, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list5, False)
        for enemy in enemy_hit_list: #You'll add another of these if you
            self.health -= 1         #want more zombies

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list6, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list7, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list8, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list9, False)
        for enemy in enemy_hit_list:
            self.health -= 1
            
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list10, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list11, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list12, False)
        for enemy in enemy_hit_list:
            self.health -= 1

        beartrap_hit_list = pygame.sprite.spritecollide(self, beartrap_list1, False)
        for beartrap in beartrap_hit_list: #Same as with zombies
            self.health -= 1

        beartrap_hit_list = pygame.sprite.spritecollide(self, beartrap_list2, False)
        for beartrap in beartrap_hit_list:
            self.health -= 1

        beartrap_hit_list = pygame.sprite.spritecollide(self, beartrap_list3, False)
        for beartrap in beartrap_hit_list:
            self.health -= 1

        #if self.health == 0: #So you can die
         #   pygame.quit()
          #  quit()

        loot_hit_list = pygame.sprite.spritecollide(self, backdoor_list, False) 
        for backdoor in loot_hit_list:
            backdoor_list.remove(backdoor)
            self.score += 1

        loot_hit_list = pygame.sprite.spritecollide(self, headlight_list, False)
        for headlight in loot_hit_list:
            headlight_list.remove(headlight)
            self.score += 1

        loot_hit_list = pygame.sprite.spritecollide(self, hood_list, False)
        for hood in loot_hit_list:
            hood_list.remove(hood)
            self.score += 1

        loot_hit_list = pygame.sprite.spritecollide(self, wheels_list, False)
        for wheels in loot_hit_list:
            wheels_list.remove(wheels)
            self.score += 1

        loot_hit_list = pygame.sprite.spritecollide(self, engine_list, False)
        for engine in loot_hit_list:
            engine_list.remove(engine)
            self.score += 1

        car_hit_list = pygame.sprite.spritecollide(self, car_list, False)
        if self.score == 5:
            for car in car_hit_list:
                car_list.remove(car)
            
                
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        # fall off the world
        if self.rect.y > worldy:
            self.health -=1
            print(self.health)
            self.rect.x = tx
            self.rect.y = ty

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0
            if self.rect.bottom <= p.rect.bottom:
               self.rect.bottom = p.rect.top
            else:
               self.movey += 3.2

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33  # how high to jump

        self.rect.x += self.movex
        self.rect.y += self.movey

class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('smol_zombie.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move1(self):
        """
        enemy movement
        """
        if enemy_list1:
            distance = 300
            speed = 2

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

    def move2(self):
        if enemy_list1:
            distance = 150
            speed = 4

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

    def move3(self):
        if enemy_list1:
            distance = 14
            speed = 50

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

    def move4(self):
        if enemy_list1:
            distance = 14
            speed = 100

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1


class Obsticale(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bear_trap-2.png')
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y         #This whole class is purely for the beartrap
        self.counter = 0



class Level:
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy - ty, tx, ty, 'base_floor_1_resize3')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level" + str(lvl))

        return ground_list

    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'smol_zombie.png')
            enemy_list1 = pygame.sprite.Group()
            enemy_list1.add(enemy)
            enemy_list2 = pygame.sprite.Group()
            enemy_list2.add(enemy)
            enemy_list3 = pygame.sprite.Group()
            enemy_list3.add(enemy)
            enemy_list4 = pygame.sprite.Group()  #This is also needed for more
            enemy_list4.add(enemy)               #enemies
            enemy_list5 = pygame.sprite.Group()
            enemy_list5.add(enemy)
            enemy_list6 = pygame.sprite.Group()
            enemy_list6.add(enemy)
            enemy_list7 = pygame.sprite.Group()
            enemy_list7.add(enemy)
            enemy_list8 = pygame.sprite.Group()
            enemy_list8.add(enemy)
            enemy_list9 = pygame.sprite.Group()
            enemy_list9.add(enemy)
            enemy_list10 = pygame.sprite.Group()
            enemy_list10.add(enemy)
            enemy_list11 = pygame.sprite.Group()
            enemy_list11.add(enemy)
            enemy_list12 = pygame.sprite.Group()
            enemy_list12.add(enemy)
        if lvl == 2:
            print("Level" + str(lvl))

        return enemy_list1
        return enemy_list2
        return enemy_list3 #This is needed for more enemies
        return enemy_list4
        return enemy_list5
        return enemy_list6
        return enemy_list7
        return enemy_list8
        return enemy_list9
        return enemy_list10
        return enemy_list11
        return enemy_list12

    def obs(lvl, bloc):
        if lvl == 1:
            beartrap = Obsticale(bloc[0], bloc[1], 'bear_trap-2.png')
            beartrap_list1 = pygame.sprite.Group()
            beartrap_list1.add(beartrap)
            beartrap_list2 = pygame.sprite.Group()
            beartrap_list2.add(beartrap)
            beartrap_list3 = pygame.sprite.Group()
            beartrap_list3.add(beartrap)
        if lvl == 2:
            print("Level" + str(lvl))

        #same as with enemies
        return beartrap_list1
        return beartrap_list2
        return beartrap_list3

    # x location, y location, img width, img height, img file
    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((-400, worldy - ty - 0, 0)) #This is for the platforms
            ploc.append((-900, worldy - ty - 500, 0)) #You can spawn more using
            ploc.append((-1000, worldy - ty - 0, 0)) #ploc.append and adding
            ploc.append((-1600, worldy - ty - 0, 0)) #values in but don't change
            ploc.append((200, worldy - ty - 128, 0)) #the worldy - ty
            ploc.append((1000, worldy - ty - 0, 0))
            ploc.append((400, worldy - ty - 256, 0))  
            ploc.append((1150, worldy - ty - 256, 0)) 
            ploc.append((1750, worldy - ty - 800, 0)) 
            ploc.append((1750, worldy - ty - 0, 0))   
            ploc.append((2350, worldy - ty - 256, 0))
            ploc.append((2950, worldy - ty - 0, 0))
            ploc.append((3550, worldy - ty - 0, 0))
            ploc.append((3080, worldy - ty - 600, 0))
            ploc.append((3850, worldy - ty - 400, 0))
            ploc.append((4150, worldy - ty - 0, 0))
            ploc.append((4750, worldy - ty - 0, 0))
            ploc.append((4600, worldy - ty - 256, 0))
            ploc.append((5350, worldy - ty - 0, 0))
            ploc.append((5950, worldy - ty - 0, 0))
            ploc.append((5700, worldy - ty - 600, 0))
            ploc.append((6550, worldy - ty - 0, 0))
            ploc.append((7150, worldy - ty - 0, 0))
            ploc.append((6950, worldy - ty - 375, 0))
            ploc.append((6950, worldy - ty - 750, 0))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'piskel_platoform1.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run' + str(i) + str(ploc[i]))
                i = i + 1

        if lvl == 2:
            print("Level" + str(lvl))


        return plat_list


    def car(lvl, cloc):
        if lvl== 1:
            car = Car(cloc[0], cloc[1], 'broken_car4.png')
            car_list = pygame.sprite.Group()
            car_list.add(car)
        if lvl == 2:
            print("level"+ str(lvl))

        return car_list
        
    def loot(lvl, hloc):
        if lvl == 1:
            backdoor = Backdoor(hloc[0], hloc[1], 'car_back_door1.png')
            backdoor_list = pygame.sprite.Group()
            backdoor_list.add(backdoor)
        if lvl == 2:
            print("level"+ str(lvl))

        return backdoor_list

    def lootb(lvl, zloc):
        if lvl == 1:
            headlight = Headlights(zloc[0], zloc[1], 'headlights_1.png')
            headlight_list = pygame.sprite.Group()
            headlight_list.add(headlight)
        if lvl == 2:
            print("level"+ str(lvl))

        return headlight_list

    def lootc(lvl, mloc):
        if lvl == 1:
            hood = Hood (mloc[0], mloc[1], 'hood_of_car.png')
            hood_list = pygame.sprite.Group()
            hood_list.add(hood)
        if lvl == 2:
            print("level"+ str(lvl))

        return hood_list

    def lootd(lvl, vloc):
        if lvl == 1:
            wheels = Wheels(vloc[0], vloc[1], 'wheels.png')
            wheels_list = pygame.sprite.Group()
            wheels_list.add(wheels)
        if lvl == 2:
            print("level"+ str(lvl))

        return wheels_list

    def loote(lvl, qloc):
        if lvl == 1:
            engine = Engine(floc[0], floc[1], 'engine3.png')
            engine_list = pygame.sprite.Group()
            engine_list.add(engine)
        if lvl == 2:
            print("level"+ str(lvl))

        return engine_list



'''
Setup
'''

backdrop = pygame.image.load('piskel_background2.png')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 30  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

eloc1 = []
eloc1 = [390, 326]
eloc2 = []
eloc2 = [1140, 326]                #Need to add more zombies/beartraps here
eloc3 = []                         #If you want more zombies/beartraps
eloc3 = [-900,582]
eloc4 = []
eloc4 = [-320, 82]
eloc5 = []
eloc5 = [1750,-150]
eloc6 = []
eloc6 = [2350, -150]
eloc7 = []
eloc7 = [1570, 582]
eloc8 = []
eloc8 = [2950, 582]
eloc9 = []
eloc9 = [6950, -100]
eloc = []
eloc10 = [6000, 582]
eloc11 = []
eloc11 = [6000, 512]
eloc12 = []
eloc12 = [6000, 444]
bloc1 = []
bloc1 = [995, 628]
bloc2 = []
bloc2 = [2930, 628]
bloc3 = [4460, 628]
cloc = [-301,406]
hloc =[-730,625]
zloc = [600,385]
mloc = [2550,389]
vloc = [4200,230]
floc = [6200,610]
enemy_list1 = Level.bad(1, eloc1)
enemy_list2 = Level.bad(1, eloc2)
enemy_list3 = Level.bad(1, eloc3)   #same as above here
enemy_list4 = Level.bad(1, eloc4)   
enemy_list5 = Level.bad(1, eloc5)
enemy_list6 = Level.bad(1, eloc6)
enemy_list7 = Level.bad(1, eloc7)
enemy_list8 = Level.bad(1, eloc8)
enemy_list9 = Level.bad(1, eloc9)
enemy_list10 = Level.bad(1,eloc10)
enemy_list11 = Level.bad(1, eloc11)
enemy_list12 = Level.bad(1, eloc12)
beartrap_list1 = Level.obs(1, bloc1)
beartrap_list2 = Level.obs(1, bloc2)
beartrap_list3 = Level.obs(1, bloc3)
car_list = Level.car(1, cloc)
backdoor_list = Level.loot(1,hloc)
headlight_list = Level.lootb(1,zloc)
hood_list = Level.lootc(1,mloc)
wheels_list =Level.lootd(1,vloc)
engine_list = Level.loote(1,floc)
gloc = []
tx = 64
ty = 64

i = 0
while i <= (worldx / tx) + tx:
    gloc.append(i * tx)
    i = i + 1

ground_list = Level.ground(1, gloc, tx, ty)
plat_list = Level.platform(1, tx, ty)

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

    keys = pygame.key.get_pressed()

    if keys[ord('w')]:
        player.jump()

    if keys[ord('a')]:
        player.control(-6,0)

    else:
        player.control(100,0)         #This is the movement and is smooth
                                      #Please don't touch it it's volatile ;(
    if keys[ord('d')]:
        player.control(6,0)

    else:
        player.control(-6,0)


    if player.rect.x >= forwardx:
        scroll = player.rect.x - forwardx
        player.rect.x = forwardx
        for p in plat_list:
            p.rect.x -= scroll
        for e in enemy_list1:
            e.rect.x -= scroll
        for e in enemy_list2:
            e.rect.x -= scroll
        for e in enemy_list3:
            e.rect.x -= scroll          #for scrolling left
        for e in enemy_list4:
            e.rect.x -= scroll
        for e in enemy_list5:
            e.rect.x -= scroll
        for e in enemy_list6:
            e.rect.x -= scroll
        for e in enemy_list7:
            e.rect.x -= scroll
        for e in enemy_list8:
            e.rect.x -= scroll
        for e in enemy_list9:
            e.rect.x -= scroll
        for e in enemy_list10:
            e.rect.x -= scroll
        for e in enemy_list11:
            e.rect.x -= scroll
        for e in enemy_list12:
            e.rect.x -= scroll
        for b in beartrap_list1:
            b.rect.x -= scroll
        for b in beartrap_list2:
            b.rect.x -= scroll
        for b in beartrap_list3:
            b.rect.x -= scroll
        for c in car_list:
            c.rect.x -= scroll
        for m in backdoor_list:
            m.rect.x -= scroll
        for q in headlight_list:
            q.rect.x -= scroll
        for o in hood_list:
            o.rect.x -= scroll
        for r in wheels_list:
            r.rect.x -= scroll
        for k in engine_list:
            k.rect.x -= scroll

    if player.rect.x <= backwardx:
        scroll = backwardx - player.rect.x
        player.rect.x = backwardx
        for p in plat_list:
            p.rect.x += scroll
        for e in enemy_list1:
            e.rect.x += scroll
        for e in enemy_list2:              #For scrolling right
            e.rect.x += scroll
        for e in enemy_list3:
            e.rect.x += scroll
        for e in enemy_list4:
            e.rect.x += scroll
        for e in enemy_list5:
            e.rect.x += scroll
        for e in enemy_list6:
            e.rect.x += scroll
        for e in enemy_list7:
            e.rect.x += scroll
        for e in enemy_list8:
            e.rect.x += scroll
        for e in enemy_list9:
            e.rect.x += scroll
        for e in enemy_list10:
            e.rect.x += scroll
        for e in enemy_list11:
            e.rect.x += scroll
        for e in enemy_list12:
            e.rect.x += scroll
        for b in beartrap_list1:
            b.rect.x += scroll
        for b in beartrap_list2:
            b.rect.x += scroll
        for b in beartrap_list3:
            b.rect.x += scroll
        for c in car_list:
            c.rect.x += scroll
        for m in backdoor_list:
            m.rect.x += scroll
        for q in headlight_list:
            q.rect.x += scroll
        for o in hood_list:
            o.rect.x += scroll
        for r in wheels_list:
            r.rect.x += scroll
        for k in engine_list:
            k.rect.x += scroll


    world.blit(backdrop, backdropbox)
    player.update()
    player.gravity()
    player_list.draw(world)
    enemy_list1.draw(world)
    enemy_list2.draw(world)         #If you add in anything and you want it to
    enemy_list3.draw(world)         #display you need to put it here. Copy
    enemy_list4.draw(world)         #the enemy_list stuff with .draw
    enemy_list5.draw(world)
    enemy_list6.draw(world)
    enemy_list7.draw(world)
    enemy_list8.draw(world)
    enemy_list9.draw(world)
    enemy_list10.draw(world)
    enemy_list11.draw(world)
    enemy_list12.draw(world)
    beartrap_list1.draw(world)
    beartrap_list2.draw(world)
    beartrap_list3.draw(world)
    car_list.draw(world)
    #headlight_list.draw(world)
    #backdoor_list.draw(world)
    #hood_list.draw(world)
    #wheels_list.draw(world)
    #engine_list.draw(world)
    ground_list.draw(world)
    plat_list.draw(world)
    for e in enemy_list1:
        e.move1()
    for e in enemy_list2:
        e.move2()
    for e in enemy_list7:
        e.move3()
    for e in enemy_list8:
        e.move4()
    pygame.display.flip()
    clock.tick(fps)

