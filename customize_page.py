import tkinter as tk
import crossword_page
import menu_page

class CustomizePage(tk.Frame):
    '''
    Page displays crossword customizer.
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
        label = tk.Label(self, text="CUSTOMIZE YOUR BOARD", font=("Courier", 20),)
        label.grid(row=0, columnspan=8, )

        menu_button = tk.Button(self, text="MENU", font=("Courier", 10),
                            command=lambda: controller.show_frame(menu_page.MenuPage))
        menu_button.grid(row=1, column=0, columnspan=2,)

        # Generates crossword, switch to CrosswordPage
        generate_button = tk.Button(self, text="GENERATE", font=("Courier", 10),
                            command=lambda: controller.show_frame(crossword_page.CrosswordPage, 
                                                                  (self.determine_layout())))
        generate_button.grid(row=1, column=2, columnspan=2)

        self.size = 7
        self.create_labels_list(self.size)
        self.display_grid(self.size)

    def create_labels_list(self, size):
        '''
        Creates a list of labels which will be the squares of our crossword.

        Parameters:
            size <int>: Height/width of grid.
        '''

        self.labels_list = []

        for i in range(size**2):
            self.labels_list.append(tk.Label(self, height=3, width=6, bg='white', relief="ridge"))

    def get_labels_lists(self):
        '''
        Returns labels_list
        '''
        return self.labels_list

    def display_grid(self, size):
        '''
        Displays a grid of specified height/width.

        Parameters:
            size <int>: Height/width of grid.
        '''
        row = 2
        column = 0
        for i in self.labels_list:
            i.grid(column=column, row=row)
            i.bind("<Button-1>",lambda e, 
                   label_to_change=i:self.change_background(label_to_change))
                   
            column += 1

            if column == size:
                column = 0
                row += 1

    def change_background(self, label_to_change):
        '''
        Changes the chosen labels background on LMB click.

        Parameters:
            label_to_change (tk): Tk button which we are changing.
        '''
        current_colour = label_to_change.cget('bg')

        if current_colour == 'black':
            label_to_change.config(bg="white")

        else:
            label_to_change.config(bg="black")

    def determine_layout(self):
        '''
        Determines the square/grid number of all the white tiles.

        Parameters:
            labels_list <list>(tk): A list of the crosswords labels.
        '''
        self.layout = []

        for i in self.labels_list:
            colour = i.cget('bg')
            if colour == 'white':
                self.layout.append(self.labels_list.index(i))

        print("LAYOUT:", self.layout)
        return self.layout

        


    
