'''
Crossword v2
'''
import tkinter as tk
from menu_page import MenuPage
from customize_page import CustomizePage
from crossword_page import CrosswordPage
import column_search
import row_search
import word_selector

class Crossword(tk.Tk):
    '''
    Crossword App object.
    Controls the display of frames.
    '''

    def __init__(self, *args, **kwargs):
        '''
        '''
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.layout = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25]

        self.frames = {}

        for F in (MenuPage, CustomizePage, CrosswordPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuPage)

    def show_frame(self, cont, *args):
        '''
        Raise frame to the top.

        Parameters:
            cont <Page>: A page object which is to be raised.
        '''
        frame = self.frames[cont]

        if args:
            self.layout = args[0]
            print(args)

        if cont == CrosswordPage:
            frame.squares = self.layout
            print(frame.squares)
            frame.display_crossword()

        frame.tkraise()
        
app = Crossword()
app.mainloop()