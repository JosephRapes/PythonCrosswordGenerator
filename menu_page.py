import tkinter as tk
import customize_page
import crossword_page

class MenuPage(tk.Frame):
    '''
    Menu page.
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
        label = tk.Label(self, text="PYCROSS", font=("Courier", 44))
        label.pack(pady=10,padx=10)

        self.random_layout = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25]

        custom_board_button = tk.Button(self, text="CUSTOM BOARD", font=("Courier", 20),
                            command=lambda: controller.show_frame(customize_page.CustomizePage))
        custom_board_button.pack()

        random_board_button = tk.Button(self, text="RANDOM BOARD", font=("Courier", 20),
                              command=lambda: controller.show_frame(
                                  crossword_page.CrosswordPage, self.random_layout))
        random_board_button.pack()