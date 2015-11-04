# -*- coding: utf-8 -*-
"""
Snake Moving Game

University of South Carolina 
CSCE206  Scientific Application Programming
Spring 2015  Final project
Created on Thu Apr 23 12:12:08 2015

Installation:  
You need to install pygame package to run this game
on linux:  pip install pygame
"""

import sys
import random
import pygame
from pygame.locals import *
import pygame.mixer
import os

time = 15
GAMEWIDTH = 900
GAMEHEIGHT = 700
size = 20
width = int(GAMEWIDTH / size)-1
height = int(GAMEHEIGHT / size)-1

BLACK     = ( 0, 0, 0)
RED       = ( 165, 42, 42)
WHITE     = ( 255, 255, 255)
GRAY      = ( 128 , 128, 128)
ORANGE   =  (255 ,  128, 0)
PURPLE   =  (175, 0, 255)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

startx='x'
starty='y'
HEAD = 0
counter = 0

image1 = pygame.image.load("cock.png")
image2 = pygame.image.load("cart.png")
image3 = pygame.image.load("paw.png")
image4 = pygame.image.load("tiger.png")
image5 = pygame.image.load("cocky.png")
image6 = pygame.image.load("bomb.png")
image7 = pygame.image.load("WASD.png")
image8 = pygame.image.load("arrowKeys.png")

def main():
    global timeCLOCK, SHOW, gamefont, gamefont2

    pygame.init()

    pygame.mixer.music.load('sand.wav')
    sound1 = pygame.mixer.Sound('sand.wav')
    pygame.mixer.music.play(10)
    sound2 = pygame.mixer.Sound('chomp.wav')
    chan1 = pygame.mixer.find_channel()
    pygame.mixer.music.set_volume(0.4)
    sound3 = pygame.mixer.Sound('boo.wav')

    timeCLOCK = pygame.time.Clock()
    SHOW = pygame.display.set_mode((GAMEWIDTH, GAMEHEIGHT))
    gamefont = pygame.font.SysFont("Arial", 32)
    gamefont2 = pygame.font.SysFont("Arial", 44)
    pygame.display.set_caption('Cockaboose')

    StartScreen()
    ControlsScreen()
    while True:
        runGame()
        EndScreen()

def getRandomLocation():
    return {'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)}

def drawCock(Cock):
    for place in Cock:
        x = place['x'] * size
        y = place['y'] * size
        CART = pygame.transform.scale(image2,(size,size))
        SHOW.blit(CART,(x,y))

    if Cock[2:]:

        HEAD = pygame.transform.scale(image1,(size,size))
        SHOW.blit(HEAD,(Cock[0]['x']*size,Cock[0]['y']*size))

def drawPaw(place):
    x = place['x'] * size
    y = place['y'] * size
    paw=pygame.transform.scale(image3,(size, size))
    SHOW.blit(paw,(x,y))

def drawBomb(bomblist):
    for bomb in bomblist:
        x = bomb['x'] * size
        y = bomb['y'] * size
        bomb=pygame.transform.scale(image6,(size, size))
        SHOW.blit(bomb,(x,y))

def runGame():
    global time, eaten, bomb
    pos = 1
    startx = 10
    starty = 10
    Cock = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    eaten = 0
    bomblist=[]
    paw = getRandomLocation()
    bomb = getRandomLocation()
    if bomb == paw:
        bomb = getRandomLocation()
        bomblist.append(bomb)
    if paw == bomb:
        paw = getRandomLocation()

    sound1 = pygame.mixer.Sound('sand.wav')
    sound2 = pygame.mixer.Sound('chomp.wav')

    while True:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    quitgame()
                elif event.key == K_p:
                    pause()
                elif event.key == K_a:
                    time += 5
                elif event.key == K_s:
                    time -= 3
                elif event.key == K_d:
                    time = 15 

        if Cock[HEAD]['x'] == -1 or Cock[HEAD]['x'] == width or Cock[HEAD]['y'] == -1 or Cock[HEAD]['y'] == height:
            return 
        for CockBody in Cock[1:]:
            if CockBody['x'] == Cock[HEAD]['x'] and CockBody['y'] == Cock[HEAD]['y']:
               return 

        if Cock[HEAD]['x'] == paw['x'] and Cock[HEAD]['y'] == paw['y']:
            paw = {'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)}
            pygame.mixer.Sound.stop(sound1)
            pygame.mixer.Sound.play(sound2)
            eaten+=1
            if eaten%3==0:
                newbomb = getRandomLocation()
                bomblist.insert(0,newbomb)
                drawBomb(bomblist)
        
        else:
            del Cock[-1] 

        for bomb in bomblist:
            if Cock[HEAD]['x'] == bomb['x'] and Cock[HEAD]['y'] == bomb['y']:
                return
            for CockBody in Cock[1:]:
                if Cock[HEAD]['x'] == bomb['x'] and Cock[HEAD]['y'] == bomb['y']:
                    return 

        if direction == UP:
            new = {'x': Cock[HEAD]['x'], 'y': Cock[HEAD]['y'] - 1}
        elif direction == DOWN:
            new = {'x': Cock[HEAD]['x'], 'y': Cock[HEAD]['y'] + 1}
        elif direction == LEFT:
            new = {'x': Cock[HEAD]['x'] - 1, 'y': Cock[HEAD]['y']}
        elif direction == RIGHT:
            new = {'x': Cock[HEAD]['x'] + 1, 'y': Cock[HEAD]['y']}
        
        Cock.insert(0, new)
        SHOW.fill(BLACK)
        drawCock(Cock)
        drawPaw(paw)
        if (len(Cock) - 3) != 0:
            drawBomb(bomblist)
        drawScore(len(Cock) - 3)
        pygame.display.update()
        timeCLOCK.tick(time)

def StartScreen():
    font = pygame.font.SysFont('Arial', 130)
    font1 = font.render('Cockaboose', True, RED)
    
    while True:
        SHOW.fill(WHITE)
        tiger = pygame.transform.scale(image4,(size*5, size*5))
        tiger = image4.convert_alpha(SHOW)
        cocky = pygame.transform.scale(image5,(size*5,size*5))
        cocky = image5.convert_alpha(SHOW)
        SHOW.blit(tiger,(GAMEWIDTH - 850, GAMEHEIGHT /3))
        
        CART = pygame.transform.scale(image2,(size*4,size*4))
        SHOW.blit(CART,(GAMEWIDTH - 750, GAMEHEIGHT/3))
        SHOW.blit(CART,(GAMEWIDTH - 650, GAMEHEIGHT/3))
        SHOW.blit(CART,(GAMEWIDTH - 550, GAMEHEIGHT/3))
        SHOW.blit(CART,(GAMEWIDTH - 450, GAMEHEIGHT/3))
        SHOW.blit(cocky,(GAMEWIDTH - 150, GAMEHEIGHT/6))
    
        show1 = pygame.transform.rotate(font1, 0)
        display1 = show1.get_rect()
        display1.center = (GAMEWIDTH / 2, GAMEHEIGHT / 8)
        SHOW.blit(show1, display1)

        drawKeyPressMsg()
        drawKeyPressPause()
        drawInstructions()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        timeCLOCK.tick(time)

def ControlsScreen():
    cfont = pygame.font.SysFont('Arial',100)
    pfont = cfont.render('Controls', True, BLACK)

    while True:
        SHOW.fill(WHITE)
        asd = pygame.transform.scale(image7,(size*10,size*6))
        SHOW.blit(asd,(GAMEWIDTH-800, GAMEHEIGHT -600))
        pygame.draw.rect(SHOW,WHITE,(165,80,100,80))

        arrows = pygame.transform.scale(image8,(size*12,size*7))
        SHOW.blit(arrows,(GAMEWIDTH-300, GAMEHEIGHT-200))

        show2 = pygame.transform.rotate(pfont, 0)
        display2 = show2.get_rect()
        display2.center = (GAMEWIDTH / 2, GAMEHEIGHT / 8)
        SHOW.blit(show2, display2)

        drawKeyPressMsg()
        drawControls()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        timeCLOCK.tick(time)


def drawKeyPressMsg():
    press = gamefont.render('Press any key to play', True, BLACK)
    press1 = press.get_rect()
    press1.bottomleft= (GAMEWIDTH - 880, GAMEHEIGHT - 17)
    SHOW.blit(press, press1)

def drawKeyPressAgain():
    press2 = gamefont.render('Press any key to try again', True, WHITE)
    press3 = press2.get_rect()
    press3.bottomleft= (GAMEWIDTH - 880, GAMEHEIGHT - 17)
    SHOW.blit(press2, press3)

def drawKeyPressContinue():
    press4 = gamefont.render('Press any key to continue', True, WHITE)
    press5 = press4.get_rect()
    press5.bottomleft= (GAMEWIDTH - 880, GAMEHEIGHT - 17)
    SHOW.blit(press4, press5)

def drawKeyPressPause():
    press6 = gamefont.render('Press P to pause at anytime', True, BLACK)
    press7 = press6.get_rect()
    press7.bottomright = (GAMEWIDTH - 20, GAMEHEIGHT - 17)
    SHOW.blit(press6, press7)

def drawInstructions():
    press8 = gamefont2.render('The CU tigers have stolen our cabooses!', True, PURPLE)
    press9 = press8.get_rect()
    press9.bottomleft = (GAMEWIDTH - 840, GAMEHEIGHT - 280)
    SHOW.blit(press8, press9)

    press10 = gamefont2.render('Collect all of the', True, PURPLE)
    press11 = press10.get_rect()
    press11.bottomleft = (GAMEWIDTH- 890, GAMEHEIGHT - 230)
    SHOW.blit(press10, press11)

    press18 = gamefont2.render(' paw prints', True, ORANGE)
    press19 = press18.get_rect()
    press19.bottomleft = (GAMEWIDTH-580, GAMEHEIGHT - 230)
    SHOW.blit(press18, press19)

    press20 = gamefont2.render(' to rebuild the train,', True, PURPLE)
    press21 = press20.get_rect()
    press21.bottomleft = (GAMEWIDTH-370, GAMEHEIGHT - 230)
    SHOW.blit(press20,press21)

    press12 = gamefont2.render('but be careful...', True, PURPLE)
    press13 = press12.get_rect()
    press13.bottomleft = (GAMEWIDTH - 600, GAMEHEIGHT -180)
    SHOW.blit(press12, press13)

    press14 = gamefont2.render('hit the edge, your caboose, or a bomb and its', True, PURPLE)
    press15 = press14.get_rect()
    press15.bottomleft = (GAMEWIDTH - 885, GAMEHEIGHT - 130)
    SHOW.blit(press14, press15)

    press16 = gamefont2.render(' GAME OVER!', True, ORANGE)
    press17 = press16.get_rect()
    press17.bottomleft = (GAMEWIDTH - 610, GAMEHEIGHT- 80)
    SHOW.blit(press16, press17)

def drawControls():
    press18 = gamefont2.render('Press A to speed up', True, RED)
    press19 = press18.get_rect()
    press19.bottomleft = (GAMEWIDTH-550, GAMEHEIGHT-490)
    SHOW.blit(press18, press19)

    press20 = gamefont2.render('Press S to slow down', True, RED)
    press21 = press18.get_rect()
    press21.bottomleft = (GAMEWIDTH-600, GAMEHEIGHT-430)
    SHOW.blit(press20, press21)

    press22 = gamefont2.render('Press D to return to normal speed', True, RED)
    press23 = press18.get_rect()
    press23.bottomleft = (GAMEWIDTH-750, GAMEHEIGHT-370)
    SHOW.blit(press22, press23)

    press24 = gamefont2.render('Use the arrow keys ', True, RED)
    press25 = press18.get_rect()
    press25.bottomleft = (GAMEWIDTH-780, GAMEHEIGHT-180)
    SHOW.blit(press24, press25)

    press25 = gamefont2.render('to change direction', True, RED)
    press26 = press18.get_rect()
    press26.bottomleft = (GAMEWIDTH-780, GAMEHEIGHT-120)
    SHOW.blit(press25, press26)

    pygame.display.update()
    timeCLOCK.tick(time)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        quitgame()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        quitgame()
    return keyUpEvents[0].key

def EndScreen():
    endfont = pygame.font.SysFont("Arial", 80)
    end1 = endfont.render('Game Over', True, RED)
    done = end1.get_rect()
    done.midtop = (GAMEWIDTH / 2, GAMEHEIGHT / 2.5)

    sound3 = pygame.mixer.Sound('boo.wav')
    sound1 = pygame.mixer.Sound('sand.wav')

    SHOW.blit(end1, done)
    drawKeyPressAgain()
    pygame.display.update()
    timeCLOCK.tick(time)
    checkForKeyPress() 

    pygame.mixer.music.pause()
    sound3.play()

    while True:
        if checkForKeyPress():
            sound3.stop()
            pygame.mixer.music.unpause()
            pygame.mixer.music.rewind()
            pygame.event.get() 
            return
def pause():
    paused=True  
    pausefont = pygame.font.SysFont("Arial", 80)
    pause1 = pausefont.render('PAUSED', True, RED)
    pone = pause1.get_rect()
    pone.midtop = (GAMEWIDTH / 2, GAMEHEIGHT / 2.5)

    pygame.mixer.music.pause()
    SHOW.blit(pause1, pone)
    drawKeyPressContinue()
    pygame.display.update()
    timeCLOCK.tick(time)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.mixer.music.unpause()
            pygame.mixer.music.rewind()
            pygame.event.get() 
            return

def drawScore(score):
    score1 = gamefont.render('Score: %s' % (score), True, RED)
    score2 = score1.get_rect()
    score2.topleft = (GAMEWIDTH - 880, 10)
    SHOW.blit(score1, score2)

def quitgame():
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()
