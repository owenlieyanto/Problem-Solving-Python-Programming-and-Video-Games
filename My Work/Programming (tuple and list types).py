'''
Write a Python program that creates an empty list and an empty tuple and then outputs them as shown in the sample run. 
The program must then input a string, use the append method to append the str object to the empty list and output the list. 
The program must then create a tuple that contains the same str object and output the tuple.

However, you cannot use the append method to append the str object to the empty tuple, since tuples are immutable. 
Instead you must use the tuple function, with the list containing the str object as an argument. 
The tuple function creates a new tuple whose elements are the same as the argument object, 
which in this case is your list containing the str object.

Note that it is possible to create your tuple using an expression list, 
instead of using the tuple function and it is possible to create your list using a list display:

my_tuple = (my_string)
my_list = [my_string]

However, for this program you must modify your empty list using append and create your tuple using the tuple function 
so you can discover how to use the append method and the tuple function.
'''

my_tuple = tuple()
my_list = []
print(my_list)
print(my_tuple)

usr_input = str(input('Enter a string >'))
my_list.append(usr_input)
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)