import tkinter as tk
import menu_page
import word_selector
import row_search
import column_search

class CrosswordPage(tk.Frame):
    '''
    Page displays a fully generated crossword.
    '''

    def __init__(self, parent, controller):
        '''
        Parameters:
            parent <tk object>: A tk 'master-frame', a parent container which 
                                all sub-containers inherit from.
            controller <Crossword object>: The parent class of the Crossword App.   
                                           Controls pages.
        '''
        tk.Frame.__init__(self, parent)

        menu_button = tk.Button(self, text="MENU",
                            command=lambda: controller.show_frame(menu_page.MenuPage))
        menu_button.grid(column=1, row=0)

        self.squares = []
        self.size = 7
        self.rows = []
        self.columns = []
        self.labels_list = []

        self.create_labels_list(self.size)

    def create_labels_list(self, size):
        '''
        Creates a list of labels which will be the squares of our crossword.

        Parameters:
            size <int>: Height/width of grid.
        '''
        for i in range(size**2):
            self.labels_list.append(tk.Label(self, height=3, 
                                             width=6, bg='white', relief="ridge"))

    def get_labels_lists(self):
        '''
        Returns labels_list
        '''
        return self.labels_list

    def display_grid(self):
        '''
        Displays a grid of specified height/width.
        '''
        row = 1
        column = 0
        for i in self.labels_list:
            i.grid(column=column, row=row)
            column += 1

            if column == self.size:
                column = 0
                row += 1

    def display_letters(self, letters, squares):
        '''
        Inserts letter into word labels.

        Parameters:
            letters <dict>: Tile number is key, letter of tile is value.
            squares <list><int>: A list of squares which make up the board.
        '''

        for i in range(len(self.labels_list)):
            if i in squares:
                self.labels_list[i].config(text=letters[i])

    def find_rows_and_columns(self):
        '''
        Finds the rows and columns of a crossword, given a list
        of available squares, and a size.
        '''
        self.rows = row_search.search(self.size, self.squares)
        self.columns = column_search.search(self.size, self.squares)

    def display_crossword(self):
        '''
        Main method for crossword generation.
        '''
        self.find_rows_and_columns()

        print("ROWS: ",self.rows)
        print("COLS: ",self.columns)
        letter_selection = word_selector.WordSelector(self.rows, self.columns)

        letters = letter_selection.select_word()
        self.display_letters(letters, self.squares)

        self.set_black_squares()

        self.display_grid()

    def set_black_squares(self):
        '''
        Changes squares colour to black.
        '''
        for i in self.labels_list:
            i.config(bg='white')

        for i in self.labels_list:
            if self.labels_list.index(i) not in self.squares:
                i.config(bg='black')


    


