# -*- coding: utf-8 -*-
"""
Guess Country Flag Game with Voice Input

University of South Carolina 
CSCE206  Scientific Application Programming
Spring 2015  Final project
Created on Thu Apr 23 12:12:08 2015
"""

import Tkinter
from Tkinter import *
from tkMessageBox import *
import pyaudio
import speech_recognition as sr

class MainWindow():

    global canvas
    global Tkinter,root,photo
    
    def __init__(self, main):

        self.imageNumber = 0
        self.correctCounter = 0
        self.wrongCounter = 0
        self.correct = "Correct"
        self.wrong = "Wrong"
        self.counter = 0

        self.canvas = Tkinter.Canvas(root)
        self.canvas.grid(row = 1, column = 2)
        
        self.button = Tkinter.Button(root, text=u"Start Game", width=10,command=self.startGame)
        self.button.grid(column=2,row=1)
        
    def startGame(self):
        
        self.canvas.grid(row = 0, column = 0)
        self.button.grid_forget()
        
        self.button.config(state="disabled")

        self.flags = []
        self.flags.append(PhotoImage(file= "flags/Germany.gif", name="Germany"))
        self.flags.append(PhotoImage(file = "flags/Argentina.gif", name="Argentina"))
        self.flags.append(PhotoImage(file = "flags/Belgium.gif", name="Belgium"))
        self.flags.append(PhotoImage(file = "flags/Spain.gif", name="Spain"))
        self.flags.append(PhotoImage(file = "flags/Ireland.gif", name="Ireland"))
        self.flags.append(PhotoImage(file = "flags/Usa.gif", name="Usa"))


        self.imageOn = self.canvas.create_image(80,130,image=self.flags[self.imageNumber], anchor='w')
    
       # self.labelVariable2 = Tkinter.StringVar()
       # self.label2 = Tkinter.Entry(root,textvariable=self.labelVariable2,width=40, justify="center")
       # self.label2.grid(column=0,row=2,columnspan=1,sticky='S',)
       # self.label2.config(state="disabled")
       # self.label2.focus_set()

        self.buttonConfirm = Tkinter.Button(root, text=u"Voice", width=10, command=self.voice, pady=1)
        self.buttonConfirm.grid(column=1,row=2)

        self.buttonNext = Tkinter.Button(root, text=u"Commands", width=10, command=self.commands)
        self.buttonNext.grid(column=1,row=1)
    
    def wrongAnswer(self, audio, answer):
        showinfo("Wrong", "You said: "+ str(audio) + "\n" +"Correct Answer: "+ str(answer))
        
        
    def showScore(self):
        showinfo("SCORE", "Correct Answers: "+ str(self.correctCounter) + "\n" +"Wrong Answers: "+ str(self.wrongCounter))
    
    def getAudio(self):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:  
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        return r.recognize(audio)
    
    def commands(self):
        showinfo("Voice Commands ", "  See next flag --> next"+ "\n \n"
                                    +"  Show Score --> show score" + "\n \n"
                                    +"  Restart Game --> restart game" + "\n"
                                    )
        
    def restartGame(self):
        
        self.imageNumber = 0
        self.correctCounter = 0
        self.wrongCounter = 0
        
        msg = Tkinter.Message(root, text="           ", width=150)
        msg.grid(column=0, row=2, sticky="E")
        msg.config(font=('times', 12, 'italic'))
        
        showinfo("Restart ", "The Game has been restarted !! ")
        
        self.canvas.itemconfig(self.imageOn, image=self.flags[self.imageNumber])
    
    def voice(self):
        
        audio = self.getAudio()
        
        if str(audio) == str(self.flags[self.imageNumber]):

            msg = Tkinter.Message(root, text=self.correct, anchor="w")
            msg.grid(column=0, row=2, sticky="E")
            msg.config(foreground="darkgreen", font=('times', 12, 'italic'))
            self.correctCounter += 1
            self.imageNumber += 1
            
            self.canvas.itemconfig(self.imageOn, image=self.flags[self.imageNumber])
            

        elif str(audio) == "show score":
                        
            self.showScore()
        
        elif str(audio) == "restart game":
            
            self.restartGame()
             
        else:

            msg = Tkinter.Message(root, text=self.wrong, anchor="w")
            msg.grid(column=0, row=2, sticky='E')
            msg.config(foreground="darkred", font=('times', 12, 'italic'))
            self.wrongAnswer(audio, self.flags[self.imageNumber])
            self.wrongCounter += 1
            self.imageNumber += 1
            
            self.canvas.itemconfig(self.imageOn, image=self.flags[self.imageNumber])

        if self.imageNumber == len(self.flags):
            self.imageNumber = 0

        
       
       # self.label2.delete(0, 'end')
       # self.label2.config(state="disabled")


root = Tkinter.Tk()
MainWindow(root)
root.mainloop()