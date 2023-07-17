#Creates ten learning agents with random chances to play eachother 10 times top 3 survive 
#Brischance variable used to inrement how manny gnereations agent has survived

from AI.Learning_player import LearningAgent
from game import Game
import random,sys,os
sys.stdout = open(os.devnull, 'w')
Agents = []
agentNumber = 1 #Number of agents created
genNumber = 1 #Number of generations
while genNumber < 1000: #Number of genertions algorithm will run for
    #create agents
    while len(Agents) < 10:
        dicts = []
        a = 0
        while a < 12: 
            tmpdict = {}
            i = 1.01
            while i > 0:
                i = round(i - 0.01,2)
                tmpdict.update({i:round(random.uniform(0, 1),2)}) 
            dicts.append(tmpdict)
            a += 1

        chances = {"pointless":dicts[0],"brispointless":dicts[1],"Jack":dicts[2],"Knight":dicts[3],'King':dicts[4],"3":dicts[5],
                        '1':dicts[6],'brisJack':dicts[7],'brisKnight':dicts[9],"brisKing":dicts[9],"bris3":dicts[10],"bris1":dicts[11]}
        Agents.append(LearningAgent(name="Agent" + str(agentNumber),brisChance=0,chance=chances))
        agentNumber += 1

    #Every Agent plays every other agent 10 times
    surviving = [] #Index of surviving agents and there performance(performance,index)
    performance = {}
    for a in Agents:
        performance.update({a.name: 0})
    x = 0
    while x < 10:
        y = x + 1
        while y < 10:
            games = 0
            while games < 10:
                briscola = ""
                deck = []
                players = [Agents[x],Agents[y]]
                game = Game(briscola, deck, players)
                winner = game.play(briscola, deck, players)
                i += 1
                if winner == Agents[x].name:
                    performance[winner] += 1
                    performance[Agents[y].name] -= 1  
                elif winner == Agents[y].name:
                    performance[winner] += 1
                    performance[Agents[x].name] -= 1  
                games += 1
            y += 1

        x += 1
    #Remove bottom seven agents
    surviving = []
    performance_copy = {}
    for p in performance:
        performance_copy.update({p: performance[p]})
    while len(surviving) < 3:
        a = max(performance, key=performance.get)
        surviving.append(a)
        performance.pop(a)
    newAgents = []
    for agent in Agents:
        if agent.name in surviving:
            newAgents.append(agent)
    Agents = newAgents
    sys.stdout = sys.__stdout__
    print("Top agents of generation " + str(genNumber) + " were" )
    print(Agents[0].name + " with a performance of " + str(performance_copy[Agents[0].name]))
    print(Agents[1].name + " with a performance of " + str(performance_copy[Agents[1].name]))
    print(Agents[2].name + " with a performance of " + str(performance_copy[Agents[2].name]))
    sys.stdout = open(os.devnull, 'w')

    for a in Agents:
        a.survivedGenertions += 1
    genNumber += 1

sys.stdout = sys.__stdout__
print("Top agents were " + Agents[0].name + " surviving " + str(Agents[0].survivedGenertions) + " generations, " + 
      Agents[1].name + " surviving " + str(Agents[1].survivedGenertions) + " generations and " + Agents[2].name + " surviving " + str(Agents[2].survivedGenertions) + " generations")
print(Agents[0].cardChances)
print(Agents[1].cardChances)
print(Agents[2].cardChances)