'''
def as_integer(an_object):
    # If the argument is a string that represents
    # a valid integer return that integer.
    # Otherwise, return the NoneType object.

def main():
    # Call the as_integer function for each
    # element in the list: ['20', 10, len, True, '-six', '-10', '0']
    # and output the result object on its own line

20
None
None
None
None
-10
0
'''

# def as_integer(an_object):
#     if isinstance(an_object, str):
#         if an_object[0] in ('-', '+'):
#             if an_object[1:].isdigit():
#                 return int(an_object)
#         if an_object.isdigit():
#             return int(an_object)
#         return None
#     return None

# def main():
#     usr_list = ['20', 10, len, True, '-six', '-10', '0']
#     for item in usr_list:
#         print(as_integer(item))

# main()


'''
def filter_ints(word_list):
    # Return a tuple containing two lists.
    # The first list should contain an int
    # for each element of the argument list
    # that is a string that represents
    # a valid integer. The second list should
    # contain all the elements of the argument
    # list that do not represent valid integers.

def main():
    # Prompt the user to enter some integers,
    # separated by blanks. Output a list of the
    # valid integers and the sum of these
    # integers. If the list contains some
    # "words" that are not valid integers, then
    # output a list of these "error words". If not,
    # do not output a list of these "error words".

The main function must input a string and split it into a list of words.
It must separate the list into two lists, one that contains all the valid integers and one that contains the invalid integers.
It must then output the integer list and the sum of its elements.
If the error list is not empty then it must also output the error list.
If the error list is empty then it should not output the error list (see the second example).

You must write a main program to test your functions but do not submit your main program.
Just copy and paste your two function definitions into the code box below.

Here are some sample runs of a main program that just calls the main function.

Enter some integers >2 4 six 8 ten 12 14
The sum of: [2, 4, 8, 12, 14] is 40
These words are not integers: ['six', 'ten']

Enter some integers >1 3 5
The sum of: [1, 3, 5] is 9
'''

def filter_ints(word_list):
    word_list_splitted = word_list.split(' ')
    list1 = []
    list2 = []

    for word in word_list_splitted:
        if isinstance(word, str):
            if word[0] in ('-', '+'):
                if word[1:].isdigit():
                    list1.append(int(word))
                else:
                    list2.append(word)
            if word.isdigit():
                list1.append(int(word))
            else:
                list2.append(word)
        else:
            list2.append(word)

    return (list1, list2)

def main():
    usr_input = input('Enter some integers >')

    (int_list, non_int_list) = filter_ints(usr_input)
    print(f'The sum of: {int_list} is {str(sum(int_list))}')

    if len(non_int_list) != 0:
        print(f'These words are not integers: {non_int_list}')

main()