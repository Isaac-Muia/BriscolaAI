from player import Player
import random

class randomAgent(Player):        
    '''An implementation of a minimax agent in the game Briscola'''

    def __init__(self, name, brisChance = 1, chance = 1):
        '''
        Initialises the agent.
        '''
        self.hand = []
        self.name = name
        self.wonCards = []
       # self.tree = [] #MINIMAX tree (Agent_card,Oponent_card,first)

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
        Picks a random card
        '''
        if len(self.hand) == 3:
            c = [0,1,2]
        elif len(self.hand) == 2:
            c = [0,1]
        else:
            return(self.hand[0])

        random.shuffle(c)

        card = self.hand[c[0]]
        self.hand.remove(card)
        return(card)

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

    def count_cards(self):
        '''returns total points of won cards'''
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
        return(points)
    
    def create_tree(self,first,card):
        '''Creates minimax tree using potential remaing cards and card played'''
        #Maximising points won
        #
        pcards = self.PotentialCards
        cardsInHand = self.cards
        tree = [] #MINIMAX tree (points,agent_card_played,oponent_card_played)
        if first:
            for card2 in pcards:

        