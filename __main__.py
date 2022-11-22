import sys, os

from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent
from human_player import Human

if len(sys.argv) < 2:
    print("Error: Usage is __main__.py 'number of games' ")
    exit(1)
if len(sys.argv) == 3:
    if sys.argv[2] == "-np":
        sys.stdout = open(os.devnull, 'w')

AgentWins = 0
AgentLosses = 0
AgentTies = 0
i = 0
#player_name = input("What is you name: ")
while i < int(sys.argv[1]):
    players = [ModelAgent(brisChance = 0.1 , chance = 0.35, name = "Model"), SimpleAgent(name = "Simple")]
    briscola = ""
    deck = []
    print("Hi")
    game = Game(briscola, deck, players)
    winner = game.play(briscola, deck, players)
    i += 1
    if winner == "Model":
        AgentWins += 1
    if winner == "Simple":
        AgentLosses += 1
    if winner == "tie":
        AgentTies += 1
sys.stdout = sys.__stdout__
print("AI wins: " + str(AgentWins))
print("AI losses: " + str(AgentLosses))
print("Ties: " + str(AgentTies))