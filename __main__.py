from tkinter import *

from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent
from human_player import Human

class Main:
    def __init__(self):
        #Create game window
        self.gameWindow=Tk(screenName="Briscola",className="Briscola")
        self.gameWindow.geometry('1600x800')

        #Input player name
        self.text=Label(self.gameWindow, text = "Your name")
        self.ent1 = Entry(self.gameWindow)

        #Diffculty setting
        self.var = IntVar() 
        self.rad1 = Radiobutton(self.gameWindow, text='Easy', variable=self.var, value=1)
        self.rad2 = Radiobutton(self.gameWindow, text='Medium', variable=self.var, value=2)
        self.rad3 = Radiobutton(self.gameWindow, text='Hard', variable=self.var, value=3) 
        self.btn=Button(text='OK',command=lambda: Main.startGame(self))
        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()
        self.text.pack()
        self.ent1.pack()
        self.btn.pack()

        self.gameWindow.mainloop()   


    def startGame(self):
        humanName = str(self.ent1.get())
        difficuty = self.var.get()
        if humanName != '' and difficuty != 0:
            #Change agent based on what difficulty was selected
            if(difficuty == 3):
                opponent = ModelAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
            elif(difficuty == 2):
                opponent = SimpleAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
            else:
                opponent = randomAgent(brisChance = 0.1 , chance = 0.35, name = "Model")
                
            #Clear GUI
            self.rad1.destroy()
            self.rad2.destroy()
            self.rad3.destroy()
            self.text.destroy()
            self.ent1.destroy()
            self.btn.destroy()  

            players = [opponent, Human(name = humanName, brisChance = 0.1 , chance = 0.35)]
            briscola = ""
            deck = []
            game = Game(briscola, deck, players,self.gameWindow,humanName)
            game.play(briscola, deck, players)
            btn2=Button(text='Back to start menu',command=lambda: Main.replay(self)).place(x = 800,y = 450)




    def replay(self):
        self.gameWindow.destroy()
        Main.__init__(self)

if __name__ == "__main__":
    m = Main()
    m.__init__()