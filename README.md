# PythonCrosswordGenerator
A simple crossword generator using Python3

I am still a begginer so any criticism would be greatly appreciated.


Currently in order to change the size you have to change self.size within the crossword_page.py and customize_page.py files.
Random generation not ready to use yet.


The algorithm for selecting words is fairly simple. 
1) The crossword is filled in order of longest to shortest words, as this is optimal for efficient solving. First we find the longest      row/column.
2) We then check the word list to find all possible words which are the same length as row/column.
3) Next we check whether the current word formats with other words already on the crossword. If so we add the word to a list of            potential candidates for the row/column.
4) After looping through word list, we choose a random word and place it into the crossword.
5) Remove the row/column from our list of empty row/columns.
6) Repeat 1 -> 5 until we find a row/column which has no potential candidates after looping through the word list. When this happens, we    remove the last succsefully placed word and repeat steps 1 -> 5. 
7) If we replaced the last words x amount of times with no progress, we remove the last 2 words.


I have used a relativley small word list to start with, around 58000 words. This limits the capabilities of the crossword when it comes to more densley packed grids. I will be updating to accommadate this larger word list soon (300000+ words, although does need some filtering): 
https://raw.githubusercontent.com/dwyl/english-words/master/words.txt


Further imporvements to efficiency will be added in the future aswell. Currently I have only sub categorized into alphabetical order; if the first square of a row/column is occupied, we only have to search through the word in the word list starting with that letter. I plan on sub-categorizing into word-length which should be another fairly significant improvement on search time.


I hate tkinter and it looks super ugly but I already kind of knew how to use it and this project was more about the logic behind solving a crossword.


Needs Improvement:

- Allow you to change the size in GUI instead of having to edit code.
- Finish random grid generation (currently only cutom works).
- Further subcategorize word list. 
- Use larger word-list.


