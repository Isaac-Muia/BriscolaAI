from sqlalchemy import false
from player import Player
import random

class LearningAgent(Player):        
    '''An AI for briscola that plays cards based on the chance variable which is a dictionary of types of cards
    (pointless,brispointless,Jack,Knight,king,3,1,brisJack,brisKnight,brisKing,bris3,bris1) of which each types
    value is a dicitonary of chances to play that card type at certain probabilites of it being beatan'''

    def __init__(self, name, brisChance, chance):
        '''
        Initialises the agent.
        '''
        self.hand = []
        self.name = name
        self.wonCards = []
        self.survivedGenertions = 0 #Generatioans survivied in genetic algorithim
        self.cardChances = chance # chance to play each card type when playing first (pointless,brispointless,Jack,Knight,king,3,1,brisJack,brisKnight,brisKing,bris3,bris1)
        self.secondCardChances = brisChance # chance to play each card  when playing second keys are every card in the game with the values being a dictionary of every card and a chance to play that card

        #List of cards still to play
        self.PotentialCards = []
        for suite in Player.suites:
            for card in Player.cards:
                self.PotentialCards.append((str(card), suite))
                

    def new_game(self, briscola,lastCard):
        '''
        initialises the game, informing the agent of the 
        briscola
        '''
        self.briscola = briscola
        self.lastCard = lastCard
        self.PotentialCards.remove(lastCard)

    def choose_card(self, briscola, first, first_card):
        '''
        Chooses card to play based on chance of playing it with current likleyhoods
        '''

        potentialHands = self.createHands()
        card_list = []
        if len(self.hand) == 1:
            cardToPLay = self.hand[0]
            self.hand.remove(cardToPLay)    
            return(cardToPLay)
        if first:
            #Gets chances of each card being beaten
            for card1 in self.hand:
                beaten = 0
                for hand in potentialHands:
                    for card in hand:
                        if self.winner(card1, card, briscola) == False:
                            beaten += 1
                            break
        
                beaten = beaten / len(potentialHands)
                card_list.append((card1,round(beaten,2)))

            #Get the type of each card in hand
            types = []
            for c in self.hand:
                if c[0] == "2" or  c[0] == "4" or c[0] == "5" or c[0] == "6" or c[0] == "7":
                    if c[1] == briscola:
                        types.append("brispointless")
                    else:
                        types.append("pointless")
                else:
                    if c[1] == briscola:
                        types.append("bris" + c[0])
                    else:
                        types.append(c[0])

            #Get the chances to play each card
            if len(self.hand) == 3:
                chancesToPLay = [self.cardChances[types[0]][card_list[0][1]],self.cardChances[types[1]][card_list[1][1]],
                                self.cardChances[types[2]][card_list[2][1]]]
                
                sum = chancesToPLay[0] + chancesToPLay[1] + chancesToPLay[2]
                if sum == 0:
                    chancesToPLay[0] = 0.33
                    chancesToPLay[1] = 0.66
                    chancesToPLay[2] = 1 
                else:
                    chancesToPLay[0] = round((chancesToPLay[0] / sum),2)
                    chancesToPLay[1] = round((chancesToPLay[0] +   chancesToPLay[1] / sum),2)
                    chancesToPLay[2] = 1

                randomChance = round(random.uniform(0.01, 0.99),2)
                if(chancesToPLay[0] > randomChance):
                    cardToPLay = self.hand[0]
                elif(chancesToPLay[1] > randomChance):
                    cardToPLay = self.hand[1]
                else:
                    cardToPLay = self.hand[2]   
            else:                                                
                chancesToPLay = [self.cardChances[types[0]][card_list[0][1]],self.cardChances[types[1]][card_list[1][1]]]  

                sum = chancesToPLay[0] + chancesToPLay[1]
                if sum == 0:
                    chancesToPLay[0] = 0.5
                    chancesToPLay[1] = 1.0
                else:
                    chancesToPLay[0] = round((chancesToPLay[0] / sum),2)
                    chancesToPLay[1] = 1

                randomChance = round(random.uniform(0.01, 0.99),2)
                if(chancesToPLay[0] > randomChance):
                    cardToPLay = self.hand[0]
                else:
                    cardToPLay = self.hand[1] 
        #Agent goes second
        else:
            #Get the chances to play each card
            if len(self.hand) == 3:
                chancesToPLay = [self.secondCardChances[briscola][first_card][self.hand[0]],self.secondCardChances[briscola][first_card][self.hand[1]],
                                self.secondCardChances[briscola][first_card][self.hand[2]]]
                sum = chancesToPLay[0] + chancesToPLay[1] + chancesToPLay[2]
                if sum == 0:
                    chancesToPLay[0] = 0.33
                    chancesToPLay[1] = 0.66
                    chancesToPLay[2] = 1 
                else:
                    chancesToPLay[0] = round((chancesToPLay[0] / sum),2)
                    chancesToPLay[1] = round((chancesToPLay[0] +   chancesToPLay[1] / sum),2)
                    chancesToPLay[2] = 1

                randomChance = round(random.uniform(0.01, 0.99),2)
                if(chancesToPLay[0] > randomChance):
                    cardToPLay = self.hand[0]
                elif(chancesToPLay[1] > randomChance):
                    cardToPLay = self.hand[1]
                else:
                    cardToPLay = self.hand[2]   
            else:                                                
                chancesToPLay =  [self.secondCardChances[briscola][first_card][self.hand[0]],self.secondCardChances[briscola][first_card][self.hand[1]]] 

                sum = chancesToPLay[0] + chancesToPLay[1]
                if sum == 0:
                    chancesToPLay[0] = 0.5
                    chancesToPLay[1] = 1.0
                else:
                    chancesToPLay[0] = round((chancesToPLay[0] / sum),2)
                    chancesToPLay[1] = 1

                randomChance = round(random.uniform(0.01, 0.99),2)
                if(chancesToPLay[0] > randomChance):
                    cardToPLay = self.hand[0]
                else:
                    cardToPLay = self.hand[1] 
        self.hand.remove(cardToPLay)    
        return(cardToPLay)

    def deal_hand(self, hand):
        ''' 
        draw cards and inform agent of their hand
        '''
        self.hand = hand
        self.PotentialCards.remove(hand[0])
        self.PotentialCards.remove(hand[1])
        self.PotentialCards.remove(hand[2])

    def draw_card(self, card):
        '''
        Draws card and updates agents hand
        '''
        if card != self.lastCard:
            self.PotentialCards.remove(card)
            
            #Other player picked up the last card so re-add it to potential cards (or i guess known cards at this point given the deck is empty)
            if len(self.PotentialCards) == 2:
                self.PotentialCards.append(self.lastCard)

        self.hand.append(card)

    def round_outcome(self, card1, card2, win):
        '''
        indicate who won and cards played
        '''
        if win:
            self.wonCards.append(card1)
            self.wonCards.append(card2)

            if card2 != self.lastCard:
                self.PotentialCards.remove(card2)

        elif card1 != self.lastCard:
            self.PotentialCards.remove(card1)

    def count_cards(self):
        '''returns total points of won cards resets class variables if game is over and hand is empty'''
        points = 0
        for card in self.wonCards:
            if card[0] == '3':
                 points += 10
            elif card[0] == '1':
                 points += 11
            elif card[0] == "Jack":
                 points += 2
            elif card[0] == "Knight":
                 points += 3
            elif card[0] == "King":
                 points += 4
        if len(self.hand) == 0:
            self.hand = []
            self.wonCards = []
            #List of cards still to play
            self.PotentialCards = []
            for suite in Player.suites:
                for card in Player.cards:
                    self.PotentialCards.append((str(card), suite))
        return(points)

    def game_outcome(self, player_win, points):
        '''
        informs the players who won and by how many points
        '''
        
    def winner(self, card1, card2, briscola):
        '''Returns true if card1 beats card2 and card1 was played first'''
        if card1[1] == card2[1]:
            if Player.cards.index(card1[0]) >  Player.cards.index(card2[0]):
                return True
            else:
                return False

        elif card1[1] == briscola: 
            return True

        elif card2[1] == briscola: 
            return False
        else:
            return True

    def createHands(self):
        '''Creates a list of potential hands of opponent'''
        potentialHands = []
        card1Index = 0
        card2 = 0
        card3 = 0
        if len(self.PotentialCards) == 2:
            potentialHands = [self.PotentialCards]
        else:
            for card1 in self.PotentialCards:
                card2 = card1Index + 1
                card3 = card1Index + 2
                while card2 < len(self.PotentialCards) - 1:
                    card3 = card2 + 1
                    while card3 < len(self.PotentialCards):
                        potentialHands.append((card1,self.PotentialCards[card2],self.PotentialCards[card3]))
                        card3 += 1
                    card2 += 1
                if card1Index == len(self.PotentialCards) - 3:
                    break
                card1Index += 1
        return(potentialHands)