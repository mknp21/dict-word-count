"""Count words in file."""
the_file = open("test.txt")

def count_words(file):
    #create a list of words in the file so we can iterate over them
    
    # word_list = []       # creates empty list to add words from the file
    word_dict = {}
    for line in file: 
        line = line.rstrip()      # removes white space and new lines on right side of line
        words = line.split(' ')     # tokenize items by space
        # word_list.append(words)    # adds a list 
           
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
    # final_list = []
    # for item in word_list[0: ]:
    #     final_list.append(item)
   



    return word_dict

print(count_words(the_file))