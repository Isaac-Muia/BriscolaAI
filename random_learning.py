#Genetic algorithm learning for model agent stops when specified number of rounds have been completed
import sys, os

from sqlalchemy import false, true
from game import Game
from human_player import Human
import random

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent



count = 0 #counts the amount of games played without changing newchance variable
briscount = 0 #counts the amount of games played without changing newbrischance variable

newBrisChance = 0.19
newChance = 0.49
winningBrisChance = 0.2
winningChance = 0.5


rounds = 0
results = []
wins = 0

while rounds < int(sys.argv[1]):
    sys.stdout = sys.__stdout__
    print("Current winning chances: " + str(winningChance) + " " + str(winningBrisChance) + "  Current Competing chances: " + str(newChance) + " " + str(newBrisChance))
    sys.stdout = open(os.devnull, 'w')
    a = 0
    AgentWins = 0
    AgentLosses = 0
    AgentTies = 0
    
    while a < 100:
        players = [ModelAgent(brisChance = winningBrisChance , chance = winningChance, name = "Winner"), ModelAgent(brisChance = newBrisChance , chance = newChance, name = "Competitor"),]
        briscola = ""
        deck = []
        game = Game(briscola, deck, players)
        winner = game.play(briscola, deck, players)
        if winner == "Winner":
            AgentWins += 1
        if winner == "Competitor":
            AgentLosses += 1
        if winner == "tie":
            AgentTies += 1
        a += 1

    #Create new chances if agent lost replace current winning chances with new chances and alternate between adjusting brisChance and chance
    if AgentWins < AgentLosses:
        k = 0
        found = False
        if wins > 1:
            for result in results:
                if result[1] == winningChance and results[2] == winningBrisChance and wins > results[0]:
                    results[k][0] = wins
                    found = True
                    break
                k += 1
            if not found:
                results.append((wins,winningChance,winningBrisChance))
            wins = 0

        winningChance = newChance
        winningBrisChance = newBrisChance
        
    else:
        wins += 1

    newBrisChance = (random.randrange(1,99) / 100)
    newChance = (random.randrange(1,99) / 100)
    rounds += 1
        
        
sys.stdout = sys.__stdout__
results.sort(reverse = True)
print(str(results))
print(winningChance,winningBrisChance)