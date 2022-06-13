from player import Player
import random

class Game:
    
    '''
    A class for maintaining the state of a game of Briscola
    '''

    def __init__(self, briscola, deck, players):
        '''Randomly chooses briscola, player order and shuffles deck 
        Returns name of winner'''   
        i = 0
        for suite in Player.suites:
            for card in Player.cards:
                deck.append((str(card), suite))
                
                i += 1
        random.shuffle(deck)
        self.briscola = deck[39][1]
        random.shuffle(players)
        players[0].new_game(briscola,deck[39])
        players[1].new_game(briscola,deck[39])

    def play(self, briscola, deck, players):
        '''Deals cards and plays a game of briscula'''
        print("Briscula is "+ self.briscola)
        print("Last card is is "+ deck[39][0] + " of " +  deck[39][1])
        deckID = 0
        hand1 = []
        hand2 = []

        #Deal starting hand
        while deckID < 6:
            hand1.append(deck[deckID])
            deckID += 1
            hand2.append(deck[deckID])
            deckID += 1

        players[0].deal_hand(hand1)
        players[1].deal_hand(hand2)

        cont = True  
        Round = 1  

        prevWinner = players[0].name
        #Plays game until players are out of cards
        while cont:

            print(Round)
            print(prevWinner + " plays first")
            print()
            if prevWinner == players[0].name:
                card1 = players[0].choose_card(self.briscola,True,None)
                print(players[0].name + " plays:")
                print(card1)
                card2 = players[1].choose_card(self.briscola,False,card1)
                print(players[1].name + " plays:")
                print(card2)

                if Game.winner(card1, card2, self.briscola):
                    players[0].round_outcome(card1,card2, True)
                    players[1].round_outcome(card1, card2, False)
                    print(players[0].name + " won")
                    prevWinner = players[0].name

                else:
                    players[0].round_outcome(card2, card1, False)
                    players[1].round_outcome(card2,card1, True)
                    print(players[1].name + " won")
                    prevWinner = players[1].name
            else:
                card1 = players[1].choose_card(self.briscola,True,None)
                print(players[1].name + " plays:")
                print(card1)
                card2 = players[0].choose_card(self.briscola,False,card1)
                print(players[0].name + " plays:")
                print(card2)

                if Game.winner(card1, card2, self.briscola):
                    players[0].round_outcome(card1,card2, False)
                    players[1].round_outcome(card1, card2, True)
                    print(players[1].name + " won")
                    prevWinner = players[1].name

                else:
                    players[0].round_outcome( card2, card1, True)
                    players[1].round_outcome( card2,card1, False)
                    print(players[0].name + " won")
                    prevWinner = players[0].name

            if deckID < 40:
                if prevWinner == players[0].name:
                    players[0].draw_card(deck[deckID])
                    deckID += 1
                    players[1].draw_card(deck[deckID])
                    deckID += 1
                    Round += 1
                else:
                    players[1].draw_card(deck[deckID])
                    deckID += 1
                    players[0].draw_card(deck[deckID])
                    deckID += 1
                    Round += 1

            elif Round < 20:
                Round += 1              
            else:
                cont = False
                return(Game.finish_game(players))


    def winner(card1, card2, briscola):
        '''Returns true if card1 beats card2'''
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

    def finish_game(players):
        '''Gets each player to count their cards and declares winner'''
        p1 = players[0].count_cards()
        p2 = players[1].count_cards()

        if p1 + p2 != 120:
            print("ERROR! Points don't equal 120")
            quit()
        if p1 > p2:
            print( players[0].name + " won by " + str(p1 - p2) + " points!")
            return(players[0].name)
        elif p2 > p1:
            print(players[1].name + " won by " + str(p2 - p1) + " points!")
            return(players[1].name)
        else:
            print("Tie!")
            return("tie")
