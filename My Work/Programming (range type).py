'''
Write a program that inputs words from the user, one per line and saves the words in a list until the user enters the word stop. 
The word stop should not be included in the list. The program should then output the list. 
It should then replace each word in the word list, whose index is even by its  index  multiplied by the length of the word. 
It should then output this modified list.

For example, here is a sample program run:

Enter a word >computer
Enter a word >science
Enter a word >university
Enter a word >alberta
Enter a word >edmonton
Enter a word >stop
['computer', 'science', 'university', 'alberta', 'edmonton']
[0, 'science', 20, 'alberta', 32]

'''

list_init = []

usr_input = input('Enter a word >')
while usr_input != 'stop':
    list_init.append(usr_input)
    usr_input = input('Enter a word >')
print(list_init)

for index in range(0, len(list_init)):
    if index % 2 == 0:
        word = list_init[index]
        list_init[index] = index * len(word)
print(list_init)
        