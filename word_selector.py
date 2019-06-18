'''
Used for selecting suitable words to fill a pre-defined crosword grid.
'''
import row_search
import column_search
import tkinter as tk
import random

SEARCH_INDEXES = {'A': [3479,3479], 'B': [3210,6689], 'C': [5493,12182], 'D': [3776,15958], 
                  'E': [2588,18546], 'F': [2557,21103], 'G': [1836,22939], 'H': [2026,24965], 
                  'I': [2673,27638], 'J': [473,28111], 'K': [354,28465], 'L': [1837,30302], 
                  'M': [2944,33246], 'N': [919,34165], 'O': [1388,35553], 'P': [4563,40116], 
                  'Q': [290,40406], 'R': [3634,44040], 'S': [6670,50710], 'T': [2881,53591], 
                  'U': [1921,55512], 'V': [811,56323], 'W': [1542,57865], 'X': [14,57879], 
                  'Y': [144,58023], 'Z': [86, 58109]}

class WordSelector():
    '''
    Selects words to fill crossword.
    '''

    def __init__(self, rows, columns):
        '''
        Parameters:
            rows <list><list>(int): List of lists. Sub-lists contain
                                    squares numbers which make each row.
            columns <list><list>(int): List of lists. Sub-lists contain
                                       squares numbers which make each column.
        '''
        self.rows = rows
        self.columns = columns
        self.grid_letters = {}
        self.used_words = []
        self.used_row_col_squares = []
        self.used_row_col = []
        self.occupied_squares = []
        self.potential_word = []
        self.current_word_intersections = []
        self.word_found = False
        self.longest_word = []
        self.column_or_row = None
        self.attempt_number = 0


    def get_longest_word(self):
        '''
        Finds longest word inside columns/rows.

        Parameters:
            columns <list><list>(int): A list containing columns (a list of label 
                                       numbers which correspond to a column).
            rows <list><list>(int): A list containing rows (a list of label numbers
                                    which correspond to a column).

        Returns:
            longest_word <list>(int): The longest row or column which has not been
                filled in yet.
            column_or_row (string): 'column' if longest word is a column, 
                                     and 'row' if row. 
        '''
        self.longest_word = []
        self.column_or_row = None

        if self.columns:
            for i in self.columns:
                if len(i) > len(self.longest_word):
                    self.longest_word = i
                    self.longest_word_type = 'column'

        if self.rows:
            for y in self.rows:
                if len(y) > len(self.longest_word):
                    self.longest_word = y
                    self.longest_word_type = 'row'


    def get_intersecting_squares(self):
        '''
        Determines the squares which are intersecting
        (are part of both a column and row).

        Returns:
            intersecting_squares <list>(int): A list of square numbers which
                                              have intersections.
        '''
        all_row_squares = [square for row in self.rows for square in row]
        all_column_squares = [square for column in self.columns for square in column]

        intersecting_squares = [square for square in all_column_squares if square in all_row_squares]

        return intersecting_squares  


    def select_word(self):
        '''
        Selects suitable words for the crossword.
        '''
        valid_word = 0

        self.get_longest_word()

        # We cannot use the get_intersecting_squares() method as it returns
        # all intersecting squares. The loop below creates a list of 
        # the indexes of the squares in our current longest word which 
        # already have a letter assigned.
        self.index_intersections = [self.longest_word.index(i) for i in 
                                    self.longest_word if i in self.occupied_squares]

        # Creates a list of our words. This is defintley
        # not needed/best but it makes sub-categorizing a bit easier.
        word_file = []
        with open('LIST_OF_CAPITAL_WORDS.txt', 'r') as f:
            for line in f:
                word_file.append(line)

        while self.columns or self.rows:
            
            # Originally we want to search through the entire list of
            # words.
            search_zone_start = 0
            search_zone_finish = 58108
            
            # If we have tried a new word 50 times, reset the counter
            # and delete the last 2 words.
            # You can change this number higher or lower and speed of
            # search will vary.
            if self.attempt_number > 20:
                self.no_word_found()
                self.no_word_found()
                self.attempt_number = 0

            # If the first letter in our word is in index_intersections
            # (already has a letter assigned to its square), we can refine
            # our word search to only words beggining with this letter.
            # Further refinement involving word length would increase the
            # efficiency of the algorithm.
            if 0 in self.index_intersections:
                search_zone_start = SEARCH_INDEXES[
                    self.grid_letters[self.longest_word[0]]][1] - SEARCH_INDEXES[
                    self.grid_letters[self.longest_word[0]]][0]

                search_zone_finish = SEARCH_INDEXES[
                    self.grid_letters[self.longest_word[0]]][1]

            for line in word_file[search_zone_start:search_zone_finish]:

                if len(line) - 1 == len(self.longest_word) and line not in self.used_words: 

                    for i in self.index_intersections:
                        if line[i] == self.grid_letters[self.longest_word[i]]:
                            valid_word += 1

                    # If the word formats, we add it to the list of
                    # potential words for that list/column.
                    if valid_word == len(self.index_intersections):
                        word_found = True
                        valid_word = 0
                        self.potential_word.append(line)
                    
                    else:
                        valid_word = 0

            if word_found:
                # print("Found word!!")

                word_found = False

                word = random.choice(self.potential_word)
                self.used_words.append(word)
                self.used_row_col_squares.append(self.longest_word)
                self.used_row_col.append(self.longest_word_type)
                print(word)

                self.potential_word = []

                for i in range(len(self.longest_word)):
                    self.grid_letters[self.longest_word[i]] = word[i] 
                    self.occupied_squares.append(self.longest_word[i])
                    
                if self.longest_word_type == 'column':
                    self.columns.remove(self.longest_word)

                elif self.longest_word_type == 'row':
                    self.rows.remove(self.longest_word)
                
                self.get_longest_word()
                self.index_intersections = [self.longest_word.index(i) for i in 
                                            self.longest_word if i in self.occupied_squares]


            else:
                self.no_word_found()

        return self.grid_letters


    def no_word_found(self):
        '''
        Back propagation for the case of no word found.
        Deletes the last word, removes it from occupied squares etc.
        '''
        print("TRYING NEW WORD")
        print(self.used_row_col)

        self.attempt_number += 1

        # Adding the row/col back to the row/col list.
        if self.used_row_col[-1] == 'row':
            self.rows.append(self.used_row_col_squares[-1])
        elif self.used_row_col[-1] == 'column':
            self.columns.append(self.used_row_col_squares[-1])

        for i in self.used_row_col_squares[-1]:
            self.occupied_squares.remove(i)

        # Find the squares in the word we are removing which 
        # are apart of another word.
        last_word_intersections = [[i for i in self.used_row_col_squares[-1] if i in y]
                                      for y in self.used_row_col_squares[:-1]]
        last_word_intersections = [item for sublist in last_word_intersections 
                                        for item in sublist]

        # Remove the squares which are apart of another word from the list.
        self.used_row_col_squares[-1] = [i for i in self.used_row_col_squares[-1] 
                                           if i not in last_word_intersections]

        for i in self.used_row_col_squares[-1]:
            del self.grid_letters[i]

        self.used_row_col_squares = self.used_row_col_squares[:-1]
        self.used_row_col = self.used_row_col[:-1]

        self.get_longest_word()
        self.index_intersections = [self.longest_word.index(i) for i in 
                                    self.longest_word if i in self.occupied_squares]
        
        print(self.attempt_number)




