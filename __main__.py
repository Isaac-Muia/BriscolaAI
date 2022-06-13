from simple_player import SimpleAgent
from human_player import Human
from random_player import randomAgent
from probability_player import ProbAgent
from simple_player_memory import ModelAgent

from game import Game
import sys
AgentWins = 0
AgentLosses = 0
AgentTies = 0
i = 0
player_name = input("What is you name: ")
while i < 1:
    players = [ModelAgent(name = "Model"),Human(name = player_name)]
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