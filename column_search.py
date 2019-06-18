'''
Searching for columns in the crossword.
'''
import tkinter as tk

def search(size, squares):
    '''
    Searches crossword for columns.

    Parameters:
        size <int>: Height/width of grid to be searched.
        squares <list><int>: A list of squares which make up the board.

    Returns:
        columns <list><list>(int): List of lists. Sub-lists contain
                                   squares numbers which make each column.
    '''

    column_edge_squares = []
    for i in range(size**2 - size, size**2):
        column_edge_squares.append(i)

    # print(column_edge_squares)

    # List of all columns
    column_list = []

    # List of squares which could potentially create a column
    current_column = []

    current_column_number = 0
    square_number = 0

    for y in range(size):
        for i in range(size):
            square_number = i*size + current_column_number

            if square_number in squares:
                

                if not len(current_column) or square_number == current_column[-1] + size:
                    
                    current_column.append(square_number)
                    
                    if square_number in column_edge_squares:
                        if len(current_column) < 3:
                            current_column = []
                        else:
                            column_list.append(current_column)
                            current_column = []
            else:
                if len(current_column) < 3:
                    current_column = []
                else:
                    column_list.append(current_column)
                    current_column = []
        
        current_column_number += 1

    print(column_list)

    return column_list


