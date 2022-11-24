from player import Player
import random
from tkinter import * 
from tkinter.ttk import * 
#from GUI import _GUI

class Game:
    
    '''
    A class for maintaining the state of a game of Briscola
    '''

    def __init__(self, briscola, deck, players,gameWindow,humanName):
        '''Randomly chooses briscola, player order and shuffles deck 
        Returns name of winner'''   
        self.gw = gameWindow #Inherit game window from main program
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

        
        #Determine which player is the human
        self.humanPlayer = 0
        if(players[1].name == humanName):
            self.humanPlayer = 1

    def play(self, briscola, deck, players):
        '''Deals cards and plays a game of briscula'''
        print("Briscula is "+ self.briscola)

        #Create canvas and list for all elemnts on screen
        self.canvas = Canvas(self.gw)
        self.elements = []
         
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
            
            self.canvas.delete('all')
            for element in self.elements:
                element.destroy()

            self.elements = []

            #Create the last card
            Game.create_card(self,self.canvas,1400,400,deck[39])

            #Create the players cards on board
            h = 0
            while h < len(players[self.humanPlayer].hand):
                Game.create_card(self,self.canvas,650 + h*150,600,players[self.humanPlayer].hand[h])
                h += 1
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

    def create_card(self,canvas,x,y,card):
        '''Puts a card on the board at the given coodinates'''
        vertical_size = 170
        horizontal_size = 130
        canvas.create_rectangle(x-horizontal_size/2, y+vertical_size/2, x+horizontal_size/2, y-vertical_size/2,
                                    outline = "black", fill = "white",
                                    width = 2)
        face = Label(self.gw,
                  text = card[0] + " of " + card[1], font = ('Arial', 13))
        self.elements.append(face)
        face.place(x = x-50, y = y-5)
        canvas.pack(fill = BOTH, expand = 1)
