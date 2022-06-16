'''
Write a program that prompts the user to enter some words as shown in the sample run. 
Then output a list that contains these words. 
Then output the input version and uppercase version of each word on the same line, separated by a space, 
as shown in the sample run:

Enter some words >The cat in the hat meets R2D2!
['The', 'cat', 'in', 'the', 'hat', 'meets', 'R2D2!']
The THE
cat CAT
in IN
the THE
hat HAT
meets MEETS
R2D2! R2D2!
'''

usr_input = input('Enter some words >')
word_list = usr_input.split(' ')
print(word_list)

for word in word_list:
    print(f'{word} {word.upper()}')