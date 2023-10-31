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
        self.cardsOnBoard = [] #List of cards on game board
        self.gw.bind("<Button-1>", Game.handle_click)
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
        self.AIPlayer = 1
        if(players[1].name == humanName):
            self.humanPlayer = 1
            self.AIPlayer = 0



    def play(self, briscola, deck, players):
        '''Deals cards and plays a game of briscula'''
        print("Briscula is "+ self.briscola)

        #Create canvas and list for all elemnts on screen
        self.canvas = Canvas(self.gw)
        global elements
        elements = []
         
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
        global round 
        round = 1  
        prevWinner = players[0].name
        while cont:
            self.humanPLayersCards = []
            self.canvas.delete('all')
            for element in elements:
                element.destroy()
            self.cardsOnBoard = []

            elements = []

            #Variable to hold what card the user wants to play (is reset to 0 after every round)
            global click_var
            click_var = IntVar()

            #Variable that is set to true when player clicks next round button
            global next_round
            next_round = BooleanVar()

        
            #Create the last card
            if(round < 18):
                Game.create_card(self,self.canvas,1400,400,deck[39],False)

            #Opponents card that is deleted when they play is random
            if round == 18:
                 deletedCard = random.randrange(0,3) 
            elif round == 19:
                deletedCard = random.randrange(0,2)
            elif round == 20:
                 deletedCard = 0
            else:
                deletedCard = random.randrange(1,4) 
            #Create the opponents  cards on the board
            a = 0
            while a < len(players[self.AIPlayer].hand):
                Game.create_card(self,self.canvas,650 + a*150,100,None,False)
                a += 1
            #Create the players cards on board
            h = 0
            while h < len(players[self.humanPlayer].hand):
                Game.create_card(self,self.canvas,650 + h*150,675,players[self.humanPlayer].hand[h],False)
                h += 1
            print(round)
            print(prevWinner + " plays first")
            print()
            if prevWinner == players[0].name:
                hand = []
                for c in  players[0].hand:
                    hand.append(c) 
                hand2 = []
                for c in  players[1].hand:
                    hand2.append(c) 
                if prevWinner != "Model":
                    while(True):
                        self.gw.wait_variable(click_var)
                        #Check player is clikcing a card that is actually on the board
                        if(click_var.get() == 1 or (click_var.get() == 2 and len(players[self.humanPlayer].hand) > 1) or 
                           (click_var.get() == 3 and len(players[self.humanPlayer].hand) > 2) ):
                            break
                    card1 = players[0].choose_card(click_var.get(),True,None)
                else:
                     card1 = players[0].choose_card(self.briscola,True,None)
                if round < 18:
                    num = hand.index(card1) + 1 #card that the oponent plays from the board
                else:
                    num = hand.index(card1)
                if players[0].name == "Model":
                    self.canvas.delete(self.cardsOnBoard[deletedCard])
                    Game.create_card(self,self.canvas,800,275,card1,True)
                else:
                    self.canvas.delete(self.humanPLayersCards.pop(num))
                    Game.create_card(self,self.canvas,800,500,card1,False)
                print(players[0].name + " plays:")
                print(card1)
                if prevWinner == "Model":
                    while(True):
                        self.gw.wait_variable(click_var)
                        #Check player is clikcing a cad that is actually on teh board
                        if(click_var.get() == 1 or (click_var.get() == 2 and len(players[self.humanPlayer].hand) > 1) or 
                           (click_var.get() == 3 and len(players[self.humanPlayer].hand) > 2) ):
                            break
                    card2 = players[1].choose_card(click_var.get(),True,None)
                else:
                     card2 = players[1].choose_card(self.briscola,True,None)
                if round > 17:
                    num2 = hand2.index(card2)
                else:
                    num2 = hand2.index(card2) + 1
                if players[0].name == "Model":
                    self.canvas.delete(self.humanPLayersCards.pop(num2))
                    Game.create_card(self,self.canvas,800,500,card2,False)
                else:
                    self.canvas.delete(self.cardsOnBoard[deletedCard])
                    Game.create_card(self,self.canvas,800,275,card2,True)
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
                hand = []
                for c in  players[1].hand:
                    hand.append(c)
                hand2 = []
                for c in  players[0].hand:
                    hand2.append(c)
                if players[1].name != "Model":
                    while(True):
                        self.gw.wait_variable(click_var)
                        #Check player is clikcing a cad that is actually on teh board
                        if(click_var.get() == 1 or (click_var.get() == 2 and len(players[self.humanPlayer].hand) > 1) or 
                           (click_var.get() == 3 and len(players[self.humanPlayer].hand) > 2) ):
                            break
                    card1 = players[1].choose_card(click_var.get(),True,None)
                else:
                     card1 = players[1].choose_card(self.briscola,True,None)
                if round < 18:
                    num = hand.index(card1) + 1 #card that the oponent plays from the board
                else:
                    num = hand.index(card1)
                if players[1].name == "Model":
                    self.canvas.delete(self.cardsOnBoard[deletedCard])
                    Game.create_card(self,self.canvas,800,275,card1,True)
                else:
                    self.canvas.delete(self.humanPLayersCards.pop(num))
                    Game.create_card(self,self.canvas,800,500,card1,False)
                print(players[1].name + " plays:")
                print(card1)
                if players[1].name == "Model":
                    while(True):
                        self.gw.wait_variable(click_var)
                        #Check player is clikcing a cad that is actually on teh board
                        if(click_var.get() == 1 or (click_var.get() == 2 and len(players[self.humanPlayer].hand) > 1) or 
                           (click_var.get() == 3 and len(players[self.humanPlayer].hand) > 2) ):
                            break
                    card2 = players[0].choose_card(click_var.get(),True,None)
                else:
                     card2 = players[0].choose_card(self.briscola,True,None)
                if round > 17:
                    num2 = hand2.index(card2)
                else:
                    num2 = hand2.index(card2) + 1
                if players[1].name == "Model":
                    self.canvas.delete(self.humanPLayersCards.pop(num2))
                    Game.create_card(self,self.canvas,800,500,card2,False)
                else:
                    self.canvas.delete(self.cardsOnBoard[deletedCard])
                    Game.create_card(self,self.canvas,800,275,card2,True)
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

            text = Label(self.gw,text = prevWinner + " Won!", font = ('Arial', 16))
            elements.append(text)
            text.place(x = 500, y =350)

            self.btn=Button(text='Next Round',command=lambda:  next_round.set(True))
            self.btn.place(x = 625, y =350)
            self.gw.wait_variable(next_round)
            self.btn.destroy()  


            if deckID < 40:
                if prevWinner == players[0].name:
                    players[0].draw_card(deck[deckID])
                    deckID += 1
                    players[1].draw_card(deck[deckID])
                    deckID += 1
                    round += 1
                else:
                    players[1].draw_card(deck[deckID])
                    deckID += 1
                    players[0].draw_card(deck[deckID])
                    deckID += 1
                    round += 1

            elif round < 20:
                round += 1              
            else:
                cont = False
                Game.finish_game(self,players)
                return


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

    def finish_game(self,players):
        '''Gets each player to count their cards and declares winner'''
        p1 = players[0].count_cards()
        p2 = players[1].count_cards()
        self.canvas.delete('all')
        global elements
        for element in elements:
            element.destroy()

        if p1 + p2 != 120:
            print("ERROR! Points don't equal 120")
            quit(1)
        if p1 > p2:
            print( players[0].name + " won by " + str(p1 - p2) + " points!")
            endText = Label(self.gw,text = players[0].name + " won by " + str(p1 - p2) + " points!", font = ('Arial', 13))
            endText.place(x = 800, y = 400)
            self.canvas.pack(fill = BOTH, expand = 1)
        elif p2 > p1:
            print(players[1].name + " won by " + str(p2 - p1) + " points!")
            endText = Label(self.gw,text = players[1].name + " won by " + str(p2 - p1) + " points!", font = ('Arial', 13))
            endText.place(x = 800, y = 400)
            self.canvas.pack(fill = BOTH, expand = 1)
        else:
            print("Tie!")
            endText = Label(self.gw,text = "Tie!", font = ('Arial', 13))
            endText.place(x = 800, y = 400)
            self.canvas.pack(fill = BOTH, expand = 1)

        
    def create_card(self,canvas,x,y,card,opponents_card):
        '''Puts a card on the board at the given coodinates
            if card is None the cards face will not be shown'''
        global elements
        vertical_size = 170
        horizontal_size = 130
        createdCard = canvas.create_rectangle(x-horizontal_size/2, y+vertical_size/2, x+horizontal_size/2, y-vertical_size/2,
                                    outline = "black", fill = "white",
                                    width = 2)
        self.cardsOnBoard.append(createdCard)
        if card != None:
            face = Label(self.gw,text = card[0] + " of " + card[1], font = ('Arial', 13))
            elements.append(face)
            face.place(x = x-50, y = y-5)
            if not opponents_card:
                 self.humanPLayersCards.append(createdCard)
        canvas.pack(fill = BOTH, expand = 1)

    def handle_click(event):
        global click_var
        global round 
        if 760 > event.y > 590 and click_var.get() == 0:
            if 715 > event.x > 585:
                click_var.set(1)
                if round > 17:
                    Game.delete_element(0)
                else:
                    Game.delete_element(1)
            elif 865 > event.x > 735:
                click_var.set(2)
                if round > 17:
                    Game.delete_element(1)
                else:
                    Game.delete_element(2)
            elif 1015 > event.x > 885:
                click_var.set(3)
                if round > 17: 
                    Game.delete_element(2)
                else:
                    Game.delete_element(3)
                
                
    def delete_element(toDelete):         
        global elements   
        new_elements = []
        k = 0
        while k < len(elements):
            if k != toDelete:
                new_elements.append(elements[k])
            else:
                elements[k].destroy()
            k += 1
        elements = new_elements