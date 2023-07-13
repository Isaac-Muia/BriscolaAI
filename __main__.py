import sys, os
from tkinter import *

from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent
from human_player import Human

if len(sys.argv) == 3:
    if sys.argv[2] == "-np":
        sys.stdout = open(os.devnull, 'w')


def startGame():
    humanName = str(ent1.get())
    difficuty = var.get()
    if humanName != '' and difficuty != 0:
        AgentWins = 0
        AgentLosses = 0
        AgentTies = 0
        i = 0
        while i < 1:
            #Change agent based on what difficulty was selected
            if(difficuty == 3):
                opponent = ModelAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
            elif(difficuty == 2):
                opponent = SimpleAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
            else:
                opponent = randomAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
            
            #Clear GUI
            rad1.destroy()
            rad2.destroy()
            rad3.destroy()
            text.destroy()
            ent1.destroy()
            btn.destroy()  

            players = [opponent, Human(name = humanName, brisChance = 0.1 , chance = 0.35)]
            briscola = ""
            deck = []
            game = Game(briscola, deck, players,gameWindow,humanName)
            winner = game.play(briscola, deck, players)
            i += 1
            if winner == "Model":
                AgentWins += 1
            if winner == humanName:
                AgentLosses += 1
            if winner == "tie":
                AgentTies += 1
        sys.stdout = sys.__stdout__
        print("AI wins: " + str(AgentWins))
        print("AI losses: " + str(AgentLosses))
        print("Ties: " + str(AgentTies))

#Create game window
gameWindow=Tk(screenName="Briscola",className="Briscola")
gameWindow.geometry('1600x800')

#Input player name
text=Label(gameWindow, text = "Your name")
ent1 = Entry(gameWindow)

#Diffculty setting
var = IntVar() 
rad1 = Radiobutton(gameWindow, text='Easy', variable=var, value=1)
rad2 = Radiobutton(gameWindow, text='Medium', variable=var, value=2)
rad3 = Radiobutton(gameWindow, text='Hard', variable=var, value=3) 
btn=Button(text='OK',command=startGame)
rad1.pack()
rad2.pack()
rad3.pack()
text.pack()
ent1.pack()
btn.pack()

#Variable to hold what card the user wants to play (is reset to 0 after every round)
click_var = IntVar()

gameWindow.mainloop()   
