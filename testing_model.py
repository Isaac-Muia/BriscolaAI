#Used for determing best chance or birschance values to use for model agent
import sys, os

from sqlalchemy import true
from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent


sys.stdout = open(os.devnull, 'w')


newBrisChance = 0.05
newChance = 0.2

results = []

while newBrisChance < 0.25: #Change to newChance if testing chance
    a = 0
    AgentWins = 0
    AgentLosses = 0
    AgentTies = 0
    
    while a < 1000:
        players = [ModelAgent(brisChance = newBrisChance , chance = newChance, name = "Model"), SimpleAgent(name = "Simple")]
        briscola = ""
        deck = []
        game = Game(briscola, deck, players)
        winner = game.play(briscola, deck, players)
        if winner == "Model":
            AgentWins += 1
        if winner == "Simple":
            AgentLosses += 1
        if winner == "tie":
            AgentTies += 1
        a += 1
    
    results.append((newBrisChance,"Wins " + str(AgentWins),"Losses " + str(AgentLosses),"Ties " + str(AgentTies)))

    newBrisChance += 0.05 #Change to newChance if testing chance
    newBrisChance = round(newBrisChance,2) #Change to newChance if testing chance
        
        
    
sys.stdout = sys.__stdout__
for result in results:
    print(str(result))