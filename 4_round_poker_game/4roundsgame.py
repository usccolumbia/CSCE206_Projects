# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import random

p1="Player 1"
p2="Player 2"

rob="Red or Black"
hol="High or Low"
iro="In Between or Out Between"
suits="Which suit will the next card be?"

def a(a):
    cp.append(a)
def b(b):
    cn.append(b)
cp=[]
a('you are a sexy beast')
a('sweet baby jesus')
a('wow slow down little player')
a('legend--wait for it--dary---legendary')
a('Geronimo!')
random.shuffle(cp)
ccp=cp[0]

cn=[]
b('better luck next time')
b('it alright, just keep trying')
b('must be realy humbling to suck on so many different level')
b('i got a call, something about treating a burn?')
random.shuffle(cn)
ccn=cn[0]

def shuffledeck():
    deck = []
    for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for n in range(2, 15):
            deck.append([n, s])
    random.shuffle(deck)
    return deck
    
def i(card):
    number=card[0]
    suit=card[1]
    map={"Diamonds":'d','Hearts':'h','Clubs':'c','Spades':'s'}
    if number<10:
        return 'Image/'+'0'+str(number)+map[suit]+'.gif'
    elif number==14:
        return 'Image/01' +map[suit]+'.gif'
    else:
        return 'Image/0'+str(number)+map[suit]+'.gif'
        
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=850, height=500)
canvas.grid(row = 20, column = 10)
bg = Tkinter.PhotoImage(file = 'Image/4roundspic.gif')
back111 = Tkinter.PhotoImage(file = 'Image/back111.gif')
canvas.create_image(425,130, image=bg)
canvas.create_image(425,280, image=back111)

e1s=[]
e2s=[]
te1=0
te2=0

def reset():
    global canvas,Tkinter,c1,c2,c3,c4,c5,c6,c7,c8,e1s,e2s,te1,te2
    global c11,c12,c13,c14,c21,c22,c23,c24,e11,e12,e13,e14,e21,e22,e23,e24
    deck = shuffledeck();
    e11=deck[1];
    e12=deck[2];
    e13=deck[3];
    e14=deck[4];
    e21=deck[5];
    e22=deck[6];
    e23=deck[7];
    e24=deck[8];
    c11 = Tkinter.PhotoImage(file = i(e11))
    c12 = Tkinter.PhotoImage(file = i(e12))
    c13 = Tkinter.PhotoImage(file = i(e13))
    c14 = Tkinter.PhotoImage(file = i(e14))
    c21 = Tkinter.PhotoImage(file = i(e21))
    c22 = Tkinter.PhotoImage(file = i(e22))
    c23 = Tkinter.PhotoImage(file = i(e23))
    c24 = Tkinter.PhotoImage(file = i(e24))
    c1 = Tkinter.PhotoImage(file = 'Image/back191.gif')
    canvas.create_image(50,430, image=c1)
    c2 = Tkinter.PhotoImage(file = 'Image/back191.gif')
    canvas.create_image(150,430, image=c2)
    c3 = Tkinter.PhotoImage(file = 'Image/back191.gif')
    canvas.create_image(250,430, image=c3)
    c4 = Tkinter.PhotoImage(file = 'Image/back191.gif')
    canvas.create_image(350,430, image=c4)
    c5 = Tkinter.PhotoImage(file = 'Image/back192.gif')
    canvas.create_image(500,430, image=c5)
    c6 = Tkinter.PhotoImage(file = 'Image/back192.gif')
    canvas.create_image(600,430, image=c6)
    c7 = Tkinter.PhotoImage(file = 'Image/back192.gif')
    canvas.create_image(700,430, image=c7)
    c8 = Tkinter.PhotoImage(file = 'Image/back192.gif')
    canvas.create_image(800,430, image=c8)
    game.set("Let the game begin!")
    ins.set("%s: Pick %s" %(p1,rob))
    s1.set("%s: 0 Point" %(p1))
    s2.set("%s: 0 Point" %(p2))
    e1s=[];
    e2s=[];
    te1=0;
    te2=0;
    s1s()
    s2s()

def cip():
    random.shuffle(cp)
    ccp=cp[0]
    game.set("%s"%(ccp))
def cin():
    random.shuffle(cn)
    ccn=cn[0]
    game.set("%s"%(ccn))

def p1s():
    global e1s,e2s,te1,te2
    e1s.append(5);
def p1l():
    e1s.append(-5);
def p1n():
    e1s.append(0);
def p2s():
    e2s.append(5);
def p2l():
    e2s.append(-5);
def p2n():
    e2s.append(0);

def s1s():
    te1=sum(e1s);
    s1.set("%s: %d Point" %(p1,te1));
def s2s():
    te2=sum(e2s);
    s2.set("%s: %d Point" %(p2,te2));

def r():
    if len(e1s) == 0 or len(e1s) == 4 or len(e1s) == 8 or len(e1s) == 12 or \
    len(e1s) == 16 or len(e1s) == 20 or len(e1s) == 24 or len(e1s) == 28 or \
    len(e1s) == 32 or len(e1s) == 36 or len(e1s) == 40 or len(e1s) == 44 or \
    len(e1s) == 48: 
        canvas.create_image(50,430, image=c11)
        ins.set( "%s: Pick %s" %(p2,rob)) 
        if e11[1] == 'Hearts' or e11[1] == 'Diamonds':
            p1s()
            cip()
        elif e11[1] == 'Spades' or e11[1] == 'Clubs':
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(500,430, image=c21)
        ins.set("%s: Pick %s" %(p1,hol))
        if e21[1] == 'Hearts' or e21[1] == 'Diamonds':
            p2s()
            cip()
        elif e21[1] == 'Spades' or e21[1] == 'Clubs':
            p2l()
            cin()
        s2s()
def b():
    if len(e1s) == 0 or len(e1s) == 4 or len(e1s) == 8 or len(e1s) == 12 or \
    len(e1s) == 16 or len(e1s) == 20 or len(e1s) == 24 or len(e1s) == 28 or \
    len(e1s) == 32 or len(e1s) == 36 or len(e1s) == 40 or len(e1s) == 44 or \
    len(e1s) == 48:
        canvas.create_image(50,430, image=c11)
        ins.set("%s: Pick %s" %(p2,rob))
        if e11[1] == 'Hearts' or e11[1] == 'Diamonds':
            p1l()
            cin()
        elif e11[1] == 'Spades' or e11[1] == 'Clubs':
            p1s()
            cip()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(500,430, image=c21)
        ins.set("%s: Pick %s" %(p1,hol))
        if e21[1] == 'Hearts' or e21[1] == 'Diamonds':
            p2l()
            cin()
        elif e21[1] == 'Spades' or e21[1] == 'Clubs':
            p2s()  
            cip()
        s2s()

def h():
    if len(e1s) == 1 or len(e1s) == 5 or len(e1s) == 9 or len(e1s) == 13 or \
    len(e1s) == 17 or len(e1s) == 21 or len(e1s) == 25 or len(e1s) == 29 or \
    len(e1s) == 33 or len(e1s) == 37 or len(e1s) == 41 or len(e1s) == 45 or \
    len(e1s) == 49:
        canvas.create_image(150,430, image=c12)
        ins.set("%s: Pick %s" %(p2,hol))
        if e12[0]>e11[0]:
            p1s()
            cip()
        elif e12[0]<e11[0]:
            p1l()
            cin()
        else:
            p1n()
            cip()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(600,430, image=c22)
        ins.set("%s: Pick %s" %(p1,iro))
        if e22[0]>e21[0]:
            p2s()
            cip()
        elif e22[0]<e21[0]:
            p2l()
            cin()
        else:
            p2n()
            cip()
        s2s()
def l():
    if len(e1s) == 1 or len(e1s) == 5 or len(e1s) == 9 or len(e1s) == 13 or \
    len(e1s) == 17 or len(e1s) == 21 or len(e1s) == 25 or len(e1s) == 29 or \
    len(e1s) == 33 or len(e1s) == 37 or len(e1s) == 41 or len(e1s) == 45 or \
    len(e1s) == 49:
        canvas.create_image(150,430, image=c12)
        ins.set("%s: Pick %s" %(p2,hol))
        if e12[0]>e11[0]:
            p1l()
            cin()
        elif e12[0]<e11[0]:
            p1s()
            cip()
        else:
            p1n()
            cip()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(600,430, image=c22)
        ins.set("%s: Pick %s" %(p1,iro))
        if e22[0]>e21[0]:
            p2l()
            cin()
        elif e22[0]<e21[0]:
            p2s()
            cip()
        else:
            p2n()
            cip()
        s2s()

def ib():
    if len(e1s) == 2 or len(e1s) == 6 or len(e1s) == 10 or len(e1s) == 14 or \
    len(e1s) == 18 or len(e1s) == 22 or len(e1s) == 26 or len(e1s) == 30 or \
    len(e1s) == 34 or len(e1s) == 38 or len(e1s) == 42 or len(e1s) == 46 or \
    len(e1s) == 50:
        canvas.create_image(250,430, image=c13)
        ins.set("%s: Pick %s" %(p2,iro))
        if e13[0] > e11[0] and e13[0] < e12[0]:
            p1s()
            cip()
        elif e13[0] < e11[0] and e13[0] > e12[0]:
            p1s()
            cip()
        elif e13[0] == e11[0] or e13[0] == e12[0]:
            p1n()
            cip()
        else:
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(700,430, image=c23)
        ins.set("%s: Pick %s" %(p1,suits))
        if e23[0] > e21[0] and e23[0] < e22[0]:
            p2s()
            cip()
        elif e23[0] < e21[0] and e23[0] > e22[0]:
            p2s()
            cip()
        elif e23[0] == e21[0] or e23[0] == e22[0]:
            p2n()
            cip()
        else:
            p2l()
            cin()
        s2s()       
def ob():
    if len(e1s) == 2 or len(e1s) == 6 or len(e1s) == 10 or len(e1s) == 14 or \
    len(e1s) == 18 or len(e1s) == 22 or len(e1s) == 26 or len(e1s) == 30 or \
    len(e1s) == 34 or len(e1s) == 38 or len(e1s) == 42 or len(e1s) == 46 or \
    len(e1s) == 50:
        canvas.create_image(250,430, image=c13)
        ins.set("%s: Pick %s" %(p2,iro))
        if e13[0] > e11[0] and e13[0] < e12[0]:
            p1l()
            cin()
        elif e13[0] < e11[0] and e13[0] > e12[0]:
            p1l()
            cin()
        elif e13[0] == e11[0] or e13[0] == e12[0]:
            p1n()
            cip()
        else:
            p1s()
            cip()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(700,430, image=c23)
        ins.set("%s: Pick %s" %(p1,suits))
        if e23[0] > e21[0] and e23[0] < e22[0]:
            p2l()
            cin()
        elif e23[0] < e21[0] and e23[0] > e22[0]:
            p2l()
            cin()
        elif e23[0] == e21[0] or e23[0] == e22[0]:
            p2n()
            cip()
        else:
            p2s()
            cip()
        s2s() 
    
def he():
    if len(e1s) == 3 or len(e1s) == 7 or len(e1s) == 11 or len(e1s) == 15 or \
    len(e1s) == 19 or len(e1s) == 23 or len(e1s) == 27 or len(e1s) == 31 or \
    len(e1s) == 35 or len(e1s) == 39 or len(e1s) == 43 or len(e1s) == 47 or \
    len(e1s) == 51:
        canvas.create_image(350,430, image=c14)
        ins.set("%s: Pick %s" %(p2,suits))
        if e14[1] == 'Hearts':
            p1s()
            cip()
        else:
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(800,430, image=c24)
        ins.set("Play again? Click Play Again esse")
        if e24[1] == 'Hearts':
            p2s()
            cip()
        else:
            p2l()
            cin()
        s2s()
def sp():
    if len(e1s) == 3 or len(e1s) == 7 or len(e1s) == 11 or len(e1s) == 15 or \
    len(e1s) == 19 or len(e1s) == 23 or len(e1s) == 27 or len(e1s) == 31 or \
    len(e1s) == 35 or len(e1s) == 39 or len(e1s) == 43 or len(e1s) == 47 or \
    len(e1s) == 51:
        canvas.create_image(350,430, image=c14)
        ins.set("%s: Pick %s" %(p2,suits))
        if e14[1] == 'Spades':
            p1s()
            cip()
        else:
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(800,430, image=c24)
        ins.set("Play again? Click Play Again esse")
        if e24[1] == 'Spades':
            p2s()
            cip()
        else:
            p2l()
            cin()
        s2s()
def cl():
    if len(e1s) == 3 or len(e1s) == 7 or len(e1s) == 11 or len(e1s) == 15 or \
    len(e1s) == 19 or len(e1s) == 23 or len(e1s) == 27 or len(e1s) == 31 or \
    len(e1s) == 35 or len(e1s) == 39 or len(e1s) == 43 or len(e1s) == 47 or \
    len(e1s) == 51:
        canvas.create_image(350,430, image=c14)
        ins.set("%s: Pick %s" %(p2,suits))
        if e14[1] == 'Clubs':
            p1s()
            cip()
        else:
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(800,430, image=c24)
        ins.set("Play again? Click Play Again esse")
        if e24[1] == 'Clubs':
            p2s()
            cip()
        else:
            p2l()
            cin()
        s2s()
def di():
    if len(e1s) == 3 or len(e1s) == 7 or len(e1s) == 11 or len(e1s) == 15 or \
    len(e1s) == 19 or len(e1s) == 23 or len(e1s) == 27 or len(e1s) == 31 or \
    len(e1s) == 35 or len(e1s) == 39 or len(e1s) == 43 or len(e1s) == 47 or \
    len(e1s) == 51:
        canvas.create_image(350,430, image=c14)
        ins.set("%s: Pick %s" %(p2,suits))
        if e14[1] == 'Diamonds':
            p1s()
            cip()
        else:
            p1l()
            cin()
        s1s()
    elif len(e1s) > len(e2s):
        canvas.create_image(800,430, image=c24)
        ins.set("Play again? Click Play Again esse")
        if e24[1] == 'Diamonds':
            p2s()
            cip()
        else:
            p2l()
            cin()
        s2s()
    
red = Tkinter.Button(root,text=u"Red",command=r)
red = canvas.create_window(5,225, anchor = NW, window = red)
black = Tkinter.Button(root,text=u"Black",command=b)
black = canvas.create_window(0,250, anchor = NW, window = black)

high = Tkinter.Button(root,text=u"High",command=h)
high = canvas.create_window(73,225, anchor = NW, window = high)
low = Tkinter.Button(root,text=u"Low",command=l)
low = canvas.create_window(75,250, anchor = NW, window = low)

ib = Tkinter.Button(root,text=u"In Between",command=ib)
ib = canvas.create_window(173,225, anchor = NW, window = ib)
ob = Tkinter.Button(root,text=u"Out Between",command=ob)
ob = canvas.create_window(170,250, anchor = NW, window = ob)

cl = Tkinter.Button(root,text=u"Clubs",command=cl)
cl = canvas.create_window(300,225, anchor = NW, window = cl)
sp = Tkinter.Button(root,text=u"Spade",command=sp)
sp = canvas.create_window(300,250, anchor = NW, window = sp)
di = Tkinter.Button(root,text=u"Diamond",command=di)
di = canvas.create_window(290,275, anchor = NW, window = di)
he = Tkinter.Button(root,text=u"Heart",command=he)
he = canvas.create_window(300,300, anchor = NW, window = he)

rs = Tkinter.Button(root,text=u"Lets Play!",command=reset)
rs = canvas.create_window(0,0, anchor = NW, window = rs)

def reset1():
    global deck,shuffledeck,e11,e12,e13,e14,e21,e22,e23,e24
    global Tkinter,c11,c12,c13,c14,c21,c22,c23,c24,e1s,e2s,te1,te2
    deck = shuffledeck();
    e11=deck[1];
    e12=deck[2];
    e13=deck[3];
    e14=deck[4];
    e21=deck[5];
    e22=deck[6];
    e23=deck[7];
    e24=deck[8];
    c11 = Tkinter.PhotoImage(file = i(e11))
    c12 = Tkinter.PhotoImage(file = i(e12))
    c13 = Tkinter.PhotoImage(file = i(e13))
    c14 = Tkinter.PhotoImage(file = i(e14))
    c21 = Tkinter.PhotoImage(file = i(e21))
    c22 = Tkinter.PhotoImage(file = i(e22))
    c23 = Tkinter.PhotoImage(file = i(e23))
    c24 = Tkinter.PhotoImage(file = i(e24))
    s1s()
    s2s()
    game.set("Let the game begin!")
    ins.set("%s: Pick %s" %(p1,rob))

rs1 = Tkinter.Button(root,text=u"Play Again?!",command=reset1)
rs1 = canvas.create_window(0,25, anchor = NW, window = rs1)

game = Tkinter.StringVar()
label1 = Tkinter.Label(root,textvariable=game,anchor="w",fg="green",bg="black")
label1.grid(column=10,row=1,columnspan=1,sticky='EW')
game.set(u"Hey Sexy, Want to Play a Game?")
ins = Tkinter.StringVar()
label1 = Tkinter.Label(root,textvariable=ins,anchor="w",fg="red",bg="white")
label1.grid(column=10,row=2,columnspan=1,sticky='EW')
ins.set(u"")

s1 = Tkinter.StringVar()
label1 = Tkinter.Label(root,textvariable=s1,anchor="w",fg="black",bg="white")
label1.grid(column=10,row=3,columnspan=1,sticky='EW')
s1.set(u"")
s2 = Tkinter.StringVar()
label1 = Tkinter.Label(root,textvariable=s2,anchor="w",fg="black",bg="white")
label1.grid(column=10,row=4,columnspan=1,sticky='EW')
s2.set(u"")

root.mainloop()