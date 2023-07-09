from tkinter import * 
from tkinter.ttk import * 
from __main__ import *

class _GUI:
    
    '''
    A class for maintaining the GUI
    '''
    def __init__(self):
        pass
    def create_card(canvas,x,y):
        '''Creats a card on the board'''
        vertical_size = 170
        horizontal_size = 130
        canvas.create_rectangle(x-horizontal_size/2, y+vertical_size/2, x+horizontal_size/2, y-vertical_size/2,
                                    outline = "black", fill = "white",
                                    width = 2)
        canvas.pack(fill = BOTH, expand = 1)