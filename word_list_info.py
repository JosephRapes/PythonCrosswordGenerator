'''
This program is used to find information about our list of words.
'''

def number_of_words_by_length():
    '''
    '''
    num_words_by_length = {}

    current_count = 0
    
    for i in range(3,25):

        with open('LIST_OF_CAPITAL_WORDS.txt', 'r') as f:

                for line in f:

                    if len(line) - 1 == i:

                        current_count += 1
                
        num_words_by_length[i] = current_count

        current_count = 0

    print(num_words_by_length)


def index_of_words_by_first_char():
    '''
    '''
    num_words_by_first_char = {}

    current_count = 0
    first_char = 'A'

    while first_char:

        with open('LIST_OF_CAPITAL_WORDS.txt', 'r') as f:

                for line in f:

                    if line[0] == first_char:

                        current_count += 1

                    else:
                        num_words_by_first_char[first_char] = current_count
                        current_count = 1
                        first_char = line[0]
                        print(num_words_by_first_char)

    print(num_words_by_first_char)
    
    sum_total = 0
    for i in num_words_by_first_char:
        sum_total += num_words_by_first_char[i]
        num_words_by_first_char[i] = sum_total

    print(num_words_by_first_char)

index_of_words_by_first_char()