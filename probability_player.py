from player import Player

class ProbAgent(Player):        
    '''An implementation of a basic AI agent in the game Briscola'''

    def __init__(self, name='Rando'):
        '''
        Initialises the agent.
        '''
        self.hand = []
        self.name = name
        self.wonCards = []

        #List of cards still to play
        self.PotentialCards = []
        i = 0
        for suite in Player.suites:
            for card in Player.cards:
                self.PotentialCards.append((str(card), suite))
                
                i += 1


    def new_game(self, briscola, lastCard):
        '''
        initialises the game, informing the agent of the 
        briscola
        '''
        self.briscola = briscola
        self.lastCard = lastCard
        self.PotentialCards.remove(lastCard)

    def choose_card(self, briscola, first, first_card):
        '''
        Chooses cards to play by playing card with highest points most likely to win
        '''

        cardToPLay = None
        if len(self.hand) == 3:
            loseRatios = [0,0,0]
        elif len(self.hand) == 2:
            loseRatios = [0,0]
        else:
            return(self.hand[0])

        #See how many potential cards in game win to cards in hand
        i = 0
        for card1 in self.hand:
            for card2 in self.PotentialCards:
                if self.winner(card1,card2,briscola):
                    loseRatios[i] += 1
            i += 1

        if first:
            #If at least one card can't be beaten play highest value unbeatable card
            cantBeat = False
            for lose in loseRatios:
                if lose == 0:
                    cantBeat = True

            if cantBeat:
                i = 0
                for card in self.hand:
                    if loseRatios[i] == 0 and (cardToPLay == None or Player.cards.index(card[0]) > Player.cards.index(cardToPLay[0])):
                        cardToPLay = card
                    i += 1
            else: 
                #Play card with highest value // loseRatio^-1
                utilities = []
                i = 0
                for card in self.hand:
                    #utilities.append((Player.cards.index(card[0]),card))
                    utilities.append((Player.cards.index(card[0]) * (loseRatios[i] ^ - 1),card))
                    i += 1
                utilities.sort()
                cardToPLay = utilities[len(utilities) - 1][1]
        else:

            #If card is above the average amount of points remaining in deck take
            avg = 0
            for card in self.PotentialCards:
                avg += Player.points[Player.cards.index(card[0])]
            avg = avg / len(self.PotentialCards)

            winningCards = []
            for card in self.hand:
                 if not self.winner(first_card, card, briscola):
                        winningCards.append(card)

            allBriscola = True
            for card in winningCards:
                if card[1] != briscola:
                    allBriscola = False

            #Pick lowest value non briscola if all cards are briscola pick lowest value one
            if Player.points[Player.cards.index(first_card[0])] >= avg and len(winningCards) != 0 and allBriscola:
                    for card in winningCards:
                        if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0])):
                            cardToPLay = card
                    else:
                        for card in winningCards:
                            if cardToPLay == None or (Player.cards.index(card[0]) < Player.cards.index(cardToPLay[0]) and card[1] != briscola) or (cardToPLay[1] == briscola and card[1] != briscola):
                                cardToPLay = card

            #Pick lowest value card with least ability to win
            else:
                allNoPoints = True
                for card in self.hand:
                    if Player.cards.index(card[0]) >= 5:
                         allNoPoints = False

                #Pick lowest value non briscola
                if not allNoPoints:
                    if Player.points[Player.cards.index(first_card[0])] >= avg and len(self.hand) != 0:
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
                    
                else:
                    prevLose = 40
                    for lose in loseRatios:
                        if lose < prevLose:
                            prevLose = lose
                    cardToPLay = self.hand[loseRatios.index(prevLose)]
        
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

            #Other player picked up the last card
            if len(self.PotentialCards) == 3:
                self.PotentialCards.append(self.lastCard)
        self.hand.append(card)

    def round_outcome(self, card1, card2, win):
        '''
        indicates if the player won and cards played (card1 is winner card)
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
        
    def winner(self, card1, card2, briscola):
        '''Returns true if card1 beats card2 when going first'''
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