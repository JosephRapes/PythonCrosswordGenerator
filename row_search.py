'''
Searching for rows in the crossword.
'''
import tkinter as tk

# [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25]

def search(size, squares):
    '''
    Searches crossword for rows.

    Parameters:
        size <int>: Height/width of grid to be searched.
        squares <list><int>: A list of squares which make up the board.

    Returns:
        rows <list><list>(int): List of lists. Sub-lists contain
                                squares numbers which make each row.
    '''

    row_edge_squares = [size-1]
    for i in range(size**2):
        if row_edge_squares[-1] + size == i:
            row_edge_squares.append(i)

    # row_edge_squares = [3,7,11,15]
    # print(row_edge_squares)

    # List of all rows
    row_list = []

    # List of squares which could potentially create a row
    current_row = []

    test_grid = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25]
    
    for i in range(size**2):
        if i in squares:
            if not len(current_row) or i == current_row[-1] + 1:
                current_row.append(i)
                if i in row_edge_squares:
                    if len(current_row) < 3:
                        current_row = []
                    else:
                        row_list.append(current_row)
                        current_row = []
        else:
            if len(current_row) < 3:
                current_row = []
            else:
                row_list.append(current_row)
                current_row = []

    print(row_list)
    
    return row_list
        
