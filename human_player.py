from player import Player
import random

class Human(Player):        
    '''An implementation of a human player in the game Briscola'''

    def __init__(self, name='Rando'):
        '''
        Initialises the agent.
        '''
        self.hand = []
        self.name = name
        self.wonCards = []

    def new_game(self, briscola,lastCard):
        '''
        initialises the game, informing the agent of the 
        briscola
        '''
        self.briscola = briscola

    def choose_card(self, briscola, first, first_card):
        '''
        allows the player to pick the card they wish to play
        '''
        print("Current hand: " + str(self.hand))
        if len(self.hand) == 1:
                return( self.hand[0])
        notDone = True
        while notDone:
            value = input("What card would you like to play? 1/2/3: ")
            if len(self.hand) == 3 and (value == '1' or   value == '2' or  value == '3'):
                notDone = False
            elif len(self.hand) == 2 and (value == '1' or   value == '2'):
                notDone = False
        card = self.hand[int(value) - 1]
        self.hand.remove(card)
        print(card)
        return(card)

    def deal_hand(self, hand):
        ''' 
        draw cards and inform agent of their hand
        '''
        self.hand = hand
        print("Current hand: " + str(hand))

    def draw_card(self, card):
        '''
        Draws card and updates agents hand
        '''
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