'''
def string_lengths(string_list):
    # Create a new list that contains the
    # lengths of the strings in the argument
    # list or an empty list if the argument list
    # is empty. Output the original list and the
    # length list.

def main():
    # Input a list of words, split it into a list
    # of words and call the string_lengths function

Enter some words >edmonton, science, computer, alberta
['edmonton,', 'science,', 'computer,', 'alberta']
[9, 8, 9, 7]

Enter some words >
[]
[]
'''

def string_lengths(string_list):
    counted_list = []
    for word in string_list:
        counted_list.append(len(word))
            
    print(string_list)
    print(counted_list)

def main():
    usr_input = input('Enter some words >')
    if usr_input == '':
        word_list = []
    else:
        word_list = usr_input.split(' ')
    string_lengths(word_list)

main()