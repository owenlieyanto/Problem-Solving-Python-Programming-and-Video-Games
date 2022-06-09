'''
Write a program that uses a list display to create a list containing the integers from 1 to 10 in increasing order, 
and outputs the list. Then prompt the user to enter a number between 1 and 10, 
replace this number by the str object gone and output the list. 
If the user enters a string that does not  represent an integer between 1 and 10, 
instead output the appropriate message that indicates this situation, as shown in the sample runs:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter an integer between 1 and 10 >5
[1, 2, 3, 4, 'gone', 6, 7, 8, 9, 10]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter an integer between 1 and 10 >15
15 is not between 1 and 10

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter an integer between 1 and 10 >hello
hello is not a positive integer
'''

list_init = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_init)

usr_input = str(input('Enter an integer between 1 and 10 >'))

if usr_input.isdigit():
    usr_input = int(usr_input)
    if usr_input in list_init:
        target_index = list_init.index(usr_input)
        list_init[target_index] = 'gone'
        print(list_init)
    else:
        print(f'{usr_input} is not between 1 and 10')
else:
    print(f'{usr_input} is not a positive integer')
