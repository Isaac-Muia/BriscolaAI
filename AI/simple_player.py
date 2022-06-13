from player import Player

class SimpleAgent(Player):        
    '''An implementation of a simple refelx agent in the game Briscola'''

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
        Chooses cards to play by maximising points for agent on definiate win and 
        giving least points otherwise also priotising not playing briscula
        '''
        cardToPLay = None
        found = False
        if not first:
            if first_card[1] != briscola or  Player.cards.index(first_card[0]) < 5:

                #Pick highest value card to win with if not briscola
                if first_card[1] != briscola:
                    for card in self.hand:
                        if not self.winner(first_card, card, briscola) and card[1] != briscola:
                            if cardToPLay == None or Player.cards.index(card[0]) > Player.cards.index(cardToPLay[0]):
                                cardToPLay = card
                                found = True

                #If agent has briscola in hand take with lowest value briscula if 1 or 3 is played
                if not found:
                    hasBriscola = False
                    for card in self.hand:
                        if card[1] == briscola:
                            hasBriscola = True

                if not found and (first_card[0] == '1' or  first_card[0] == '3' and hasBriscola):
                    for card in self.hand:
                        if card[1] == briscola:
                            if cardToPLay == None or Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]):
                                cardToPLay = card
                                found = True

                #Pick lowest value non briscola otherwise
                if not found:
                    for card in self.hand:
                        if card[1] != briscola:
                            if cardToPLay == None or  cardToPLay[1] == briscola or Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]):
                                cardToPLay = card

                        else:
                            if cardToPLay == None or (cardToPLay[1] == briscola and (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]) > Player.cards.index(first_card[0]))):
                                cardToPLay = card
            #If briscola is played that has points try win with lowest briscola else place lowest value card
            else:
                winningCards = []
                for card in self.hand:
                    if not self.winner(first_card, card, briscola):
                            winningCards.append(card)

                #Pick lowest value winning card
                if len(winningCards) != 0:
                    for card in winningCards:
                        if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0])):
                            cardToPLay = card

                if cardToPLay == None:
                    for card in self.hand:
                        if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]) and card[1] != briscola):
                            cardToPLay = card

        #Pick lowest value non briscola if going first
        else:
            allBriscola = True
            for card in self.hand:
                if card[1] != briscola:
                    allBriscola = False
            #If all cards are briscola pick lowest value one
            if allBriscola:
                for card in self.hand:
                    if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0])):
                        cardToPLay = card
            else:
                for card in self.hand:
                    if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]) and card[1] != briscola) or (cardToPLay[1] == briscola and card[1] != briscola):
                         cardToPLay = card
 #       print("Hand:")
 #       print(self.hand)   
 #       print("cardToPLay:")
  #      print(cardToPLay)
        self.hand.remove(cardToPLay)
        
        return(cardToPLay)

    def deal_hand(self, hand):
        ''' 
        draw cards and inform agent of their hand
        '''
        self.hand = hand

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

    def game_outcome(self, player_win, points):
        '''
        informs the players who won and by how many points
        '''
        
    def winner(self, card1, card2, briscola):
        '''Returns true if card1 beats card2 and card1 wwas played first'''
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