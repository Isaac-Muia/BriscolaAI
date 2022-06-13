from game import Game
import sys
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent

if len(sys.argv) != 2:
    print("Error: Usage is __main__.py 'number of games' ")
    exit(1)

AgentWins = 0
AgentLosses = 0
AgentTies = 0
i = 0
#player_name = input("What is you name: ")
while i < int(sys.argv[1]):
    players = [ModelAgent(name = "Model"), SimpleAgent(name = "Simple")]
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
print("AI wins: " + str(AgentWins))
print("AI losses: " + str(AgentLosses))
print("Ties: " + str(AgentTies))