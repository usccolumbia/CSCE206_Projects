#University of South Carolina 
#CSCE206  Scientific Application Programming
#Fall 2014  Final project
#Poker game



import Tkinter
from Tkinter import *

import random

def shuffledeck():
    deck = []
    for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for n in range(2, 15):
            deck.append([n, s])
    random.shuffle(deck)
    return deck

def cardnumber(card):
    if card == 11:
        return 'Jack'
    elif card == 12:
        return 'Queen'
    elif card == 13:
        return 'King'
    elif card == 14:
        return 'Ace'
    else:
        return str(card)

def deal(deck):
    return deck[::2], deck[1::2]

def play(Jeffrey, siri):
    if Jeffrey > siri:
        return 'Jeffrey'
    elif siri > Jeffrey:
        return 'siri'
    else:
        return 'Tie'

def refill(cardswon):
    random.shuffle(cardswon)
    return cardswon

deck = shuffledeck()
Jeffreycards, siricards = deal(deck)
inplay = []
round = 0
Jeffreywon = []
siriwon = []


root = Tkinter.Tk()

canvas = Tkinter.Canvas(root)
canvas.grid(row = 0, column = 0)

def getImageName(card):
    number=card[0]
    suit=card[1]
    map={"Diamonds":'d','Hearts':'h','Clubs':'c','Spades':'s'}
    if number<10:
        return 'Image/'+'0'+str(number)+map[suit]+'.gif'
    elif number==14:
        return 'Image/01' +map[suit]+'.gif'
    else:
        return 'Image/'+str(number)+map[suit]+'.gif'



def OnButtonClick():
    global labelVariable
    global Jeffreywon,siriwon,inplay,deck,round,Jeffreycards, siricards,Tkinter,root,photo1,photo
    global canvas
    if len(Jeffreycards) == 0 or len(siricards) == 0:
        if len(Jeffreycards) > len(siricards):
            labelVariable.set("Jeffrey has won the game!")
        elif len(siricards) > len(Jeffreycards):
            labelVariable.set("siri has won the game!")
        # labelVariable.set("game over")
        return
    round += 1
    labelVariable.set( "Time for Round %d" % round)
    Jeffreycard = Jeffreycards.pop(0)
    siricard = siricards.pop(0)



    # print Jeffreycard, siricard
    photo = Tkinter.PhotoImage(file = getImageName(Jeffreycard))
    canvas.create_image(50,130, image=photo) 
    photo1=Tkinter.PhotoImage(file = getImageName(siricard))
    canvas.create_image(200,130, image=photo1)

    inplay.extend([Jeffreycard, siricard])
    labelVariable.set( "Jeffrey flips the %s of %s." % (cardnumber(Jeffreycard[0]), Jeffreycard[1]))
    labelVariable.set( "siri flips the %s of %s." % (cardnumber(siricard[0]), siricard[1]))
    roundwinner = play(Jeffreycard[0], siricard[0])
    if roundwinner == 'Jeffrey':
        labelVariable1.set( "Jeffrey wins this round!")
        Jeffreywon.extend(inplay)
        inplay = []
    elif roundwinner == 'siri':
        labelVariable1.set( "siri wins this round!")
        siriwon.extend(inplay)
        inplay = []
    elif roundwinner == 'Tie':
        labelVariable1.set( "Jeffrey and siri have tied!")
    labelVariable.set( " %s cards            %s cards." % (len(Jeffreywon)+len(Jeffreycards), len(siriwon)+len(siricards)))
    if len(Jeffreycards) == 0 and len(Jeffreywon) > 0:
        Jeffreycards = refill(Jeffreywon)
        Jeffreywon = []
    if len(siricards) == 0 and len(siriwon) > 0:
        siricards = refill(siriwon)
        siriwon = []
           











photo = Tkinter.PhotoImage(file = 'Image/back111.gif')
canvas.create_image(50,130, image=photo)
photo1 = Tkinter.PhotoImage(file = 'Image/back111.gif')
canvas.create_image(200,130, image=photo1)

# photo1=Tkinter.PhotoImage(file = 'Image/01h.gif')
# canvas.create_image(150,100, image=photo1)

button = Tkinter.Button(root,text=u"Play another round",
                                command=OnButtonClick)
button.grid(column=1,row=0)

labelVariable = Tkinter.StringVar()
label = Tkinter.Label(root,textvariable=labelVariable,anchor="w",fg="black",bg="white")
label.grid(column=0,row=6,columnspan=2,sticky='EW')
labelVariable.set(u"Let's Play!")

labelVariable1 = Tkinter.StringVar()
label1 = Tkinter.Label(root,textvariable=labelVariable1,anchor="w",fg="black",bg="white")
label1.grid(column=0,row=5,columnspan=1,sticky='EW')
labelVariable1.set(u"Hello!")

labelVariable2 = Tkinter.StringVar()
label2 = Tkinter.Label(root,textvariable=labelVariable2,anchor='w',fg="black",bg="white")
label2.grid(column=0,row=1,columnspan=1,sticky='EW')
labelVariable2.set(u"      Jeffrey                     Siri ")

root.mainloop()