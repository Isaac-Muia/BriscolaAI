class Player:
    '''An abstract super class for a player in Briscola'''

    '''Suites and cards in a deck for briscola and points for each card'''
    suites = ["Suns", "Swords", "Clubs", "Cups"]
    cards = ['2','4','5','6','7',"Jack","Knight","King",'3','1']
    points = [0,0,0,0,0,2,3,4,10,11]
            

    def __init__(self, name):
        '''
        Initialises the agent, and gives it a name
        '''
        self.name = name

    def __str__(self):
        '''
        Returns a string represnetation of the agent
        '''
        return 'Player '+self.name

    def __repr__(self):
        '''
        returns a representation of the state of the agent.
        default implementation is just the name, but this may be overridden for debugging
        '''
        return self.__str__()

    def new_game(self,briscola,lastCard):
        '''
        initialises the game, 
        '''
        pass

    def choose_card(self, briscola):
        '''Method to choose which cards to play and then discard it from hand'''
        pass

    def deal_hand(self, hand):
        ''' Deals first hand and inform agent of their hand'''
        pass

    def draw_card(self, hand):
        '''Draws card and updates agents hand'''
        pass

    def round_outcome(self, win, card1, card2):
        '''
        indicate who won and cards played
        '''
        pass
    
    def count_cards():
        '''counts total points of won cards'''
        pass
    
    def game_outcome(self, player_win, points):
        '''
        informs the players who won and by how many points
        '''
        pass
