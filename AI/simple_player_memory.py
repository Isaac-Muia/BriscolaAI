from sqlalchemy import false
from player import Player

class ModelAgent(Player):        
    '''An implementation of a model-based reflex agent for the game Briscola.
        Chance variable determines at what likelihood of a card being taken
        the agent will play that card if it goes first (brisChance for briscola cards)'''

    def __init__(self, name, brisChance, chance):
        '''
        Initialises the agent.
        '''
        self.hand = []
        self.name = name
        self.wonCards = []
        self.brisChance = brisChance #Play briscola card if it have a below 'brisChance' chance of losing
        self.chance = chance #Play non-briscola card if it have a below 'chance' chance of losing

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
        Chooses cards to play by maximising points for agent on definiate win and 
        giving least points otherwise also priotising not playing briscula
        '''
        cardToPLay = None
        found = False
        potentialHands = self.createHands()
        if len(self.hand) == 1:
            cardToPLay = self.hand[0]

        elif not first:
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

        #Pick highest value card with chance being beaten < chance
        else:
            card_list = [] #(card,chance of being beaten)
            if len(self.hand) == 3:
                hand_list = [0,0,0]
            else:
                 hand_list = [0,0]

            #sort hand by points
            for c in self.hand:
                if hand_list[0] == 0:
                    hand_list[0] = c
                elif Player.cards.index(c[0]) > Player.cards.index(hand_list[0][0]): 
                    if len(hand_list) == 3:
                        hand_list[2] = hand_list[1]
                        hand_list[1] = hand_list[0]
                        hand_list[0] = c
                    else:
                        hand_list[1] = hand_list[0]
                        hand_list[0] = c
                elif hand_list[1] == 0:
                     hand_list[1] = c
                elif Player.cards.index(c[0]) > Player.cards.index(hand_list[1][0]): 
                     if len(hand_list) == 3:
                        hand_list[2] = hand_list[1]
                        hand_list[1] = c
                else:
                    hand_list[len(hand_list) - 1] = c

            #Gets chances of each card being beaten
            for card1 in hand_list:
                beaten = 0
                for hand in potentialHands:
                    for card in hand:
                        if self.winner(card1, card, briscola) == False:
                            beaten += 1
                            break
      
                beaten = beaten / len(potentialHands)
                card_list.append((card1,beaten))

            #Get first card with less than chance or bricola less than brischance chance to be between, pick the last card if if the first two are over 0.5
            for cardb in card_list:
                if cardb == card_list[len(card_list) - 1]:
                    cardToPLay = cardb[0]

                elif cardb[1] < self.brisChance:
                    cardToPLay = cardb[0]
                    break

                elif cardb[0][1] != briscola and cardb[1] < self.chance:
                    cardToPLay = cardb[0]
                    break


                
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