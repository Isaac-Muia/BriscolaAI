#Used for determing best chance or birschance values to use for model agent against a simple agent
#Puts results in a csv file
import sys, os

from sqlalchemy import true
from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent


sys.stdout = open(os.devnull, 'w')
file = open("results.csv", "w")

file.write("Chance,Briscola Chance,Wins,Losses,Ties\n")


newChance = 0.20

newBrisChance = 0.95
while newBrisChance > 0.01:
    newChance = 0.95
    while newChance > 0.01:
        a = 0
        AgentWins = 0
        AgentLosses = 0
        AgentTies = 0
        
        while a < 100:
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
        
        file.write((str(newChance) + ',' +  str(newBrisChance) + ',' + str(AgentWins) + ',' + str(AgentLosses) + ',' + str(AgentTies) + '\n'))
        
        newChance -= 0.05 
        newChance = round(newChance,2)
    
    newBrisChance -= 0.05
    newBrisChance = round(newBrisChance,2) 
            

sys.stdout = sys.__stdout__
file.close()