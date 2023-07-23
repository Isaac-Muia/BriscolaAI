#Creates ten learning agents with random chances to play eachother 10 times top 3 survive 
#Brischance variable used to inrement how manny gnereations agent has survived
import random,sys,os

from AI.Learning_player import LearningAgent
from  AI.simple_player_memory import ModelAgent
from game import Game
from player import Player

def modifyNumber(num):
    '''Adds or minus a random float from 0 to 0.1 from the given number and returns it
       returns 0 if number ends up negative or 1 if number ends up above 1'''
    num += round(random.uniform(-0.1, 0.1),2)
    if num > 1.0:
        num = 1.0
    elif num < 0.0:
        num = 0.0
    return(num)

sys.stdout = open(os.devnull, 'w')
Agents = []
agentNumber = 1 #Number of agents created
genNumber = 1 #Number of generations
while genNumber <= 3: #Number of genertions algorithm will run for
    #create agents
    while len(Agents) < 10:
        dicts = []#chances of playing cards when playing second
        secondChances = {}#chances of playing cards when playing first
        if genNumber == 1 or len(Agents) < 4: #Make random agents
            a = 0
            while a < 12: 
                tmpdict = {}
                i = 1.01
                while i > 0:
                    i = round(i - 0.01,2)
                    tmpdict.update({i:round(random.uniform(0, 1),2)}) 
                dicts.append(tmpdict)
                a += 1
            b = 0
            for briscola in Player.suites:
                tmpdict2 = {}
                for suite in Player.suites:
                    for card in Player.cards:
                        tmpdict = {}
                        for suite2 in Player.suites:
                            for card2 in Player.cards:
                                tmpdict.update({(card2,suite2):round(random.uniform(0, 1),2)}) 
                        tmpdict2.update({(card,suite): tmpdict})
                secondChances.update({briscola: tmpdict2})
            firstChances = {"pointless":dicts[0],"brispointless":dicts[1],"Jack":dicts[2],"Knight":dicts[3],'King':dicts[4],"3":dicts[5],
                            '1':dicts[6],'brisJack':dicts[7],'brisKnight':dicts[9],"brisKing":dicts[9],"bris3":dicts[10],"bris1":dicts[11]}
            Agents.append(LearningAgent(name="RandomAgent" + str(agentNumber),brisChance=secondChances,chance=firstChances))
        
        else:  #Make agents based on previous top three agents[0],agents[1] and agents[2]
            agentToModify = 0
            if len(Agents) > 5:
                agentToModify = 1
            elif len(Agents) > 7:
                agentToModify = 2
            secondChances = Agents[agentToModify].secondCardChances 
            firstChances = Agents[agentToModify].cardChances 
            a = 0
            while a < 12: 
                tmpdict = {}
                i = 1.01
                while i > 0:
                    i = round(i - 0.01,2)
                    firstChances["pointless"][i] = modifyNumber(firstChances["pointless"][i])
                a += 1
            for briscola in Player.suites:
                for suite in Player.suites:
                    for card in Player.cards:
                        tmpdict = {}
                        for suite2 in Player.suites:
                            for card2 in Player.cards:
                                secondChances[briscola][(card,suite)][(card2,suite2)] = modifyNumber(secondChances[briscola][(card,suite)][(card2,suite2)])
            Agents.append(LearningAgent(name="Agent" + str(agentNumber),brisChance=secondChances,chance=firstChances))
            
        agentNumber += 1

    #Every Agent plays every other agent 10 times
    surviving = [] #Index of surviving agents and there performance(performance,index)
    performance = {}
    for a in Agents:
        performance.update({a.name: 0})
    x = 0
    while x < 10:
      #  y = x + 1
      #  while y < 10:
            games = 0
            while games < 20:
                briscola = ""
                deck = []
                players = [Agents[x],ModelAgent(name="Model",brisChance=0.1,chance=0.35)]
                game = Game(briscola, deck, players)
                winner = game.play(briscola, deck, players)

                if winner == Agents[x].name:
                    performance[winner] += 1
             #       performance[Agents[y].name] -= 1  
            #    elif winner == Agents[y].name:
            #        performance[winner] += 1
              #      performance[Agents[x].name] -= 1  
                else:
                    performance[Agents[x].name] -= 1

                games += 1
         #   y += 1

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
#print(Agents[0].cardChances)
#print(Agents[0].secondCardChances)
#print()
#print(Agents[1].cardChances)
#print(Agents[1].secondCardChances)
#print()
#print(Agents[2].cardChances)
#print(Agents[2].secondCardChances)
file1 = open(Agents[0].name +".txt", "w")
file1.write(str(Agents[0].cardChances) + '\n\n' + str(Agents[0].secondCardChances))
file2 = open(Agents[1].name +".txt", "w")
file2.write(str(Agents[1].cardChances) + '\n\n' + str(Agents[1].secondCardChances))
file2 = open(Agents[2].name +".txt", "w")
file2.write(str(Agents[2].cardChances) + '\n\n' + str(Agents[2].secondCardChances))

