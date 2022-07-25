'''
def append_fibonacci(integer_list):
    # Modify the argument list of integers by
    # appending a new integer that is the sum
    # of the last two integers in the list.
    # If the list has fewer than two elements
    # add the int object 1 to the list.
    
def main():
    # Call the append_fibonacci function on this
    # list: [3, 5, 8] and output the result object

Here is a sample run of a main program that just calls the main function.
[3, 5, 8, 13]
'''

def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        integer_list.append(1)
    else:
        last1_fib = integer_list[-1]
        last2_fib = integer_list[-2]
        integer_list.append(last1_fib + last2_fib)

def main():
    usr_list = [3, 5, 8]
    append_fibonacci(usr_list)
    print(usr_list)
    
main()


'''
def append_fibonacci(integer_list):
    # Modify the argument list of integers by
    # appending a new integer that is the sum
    # of the last two integers in the list.
    # If the list has fewer than two elements
    # add the int object 1 to the list.

def fibonacci(max):
    # Return a list that contains all Fibonacci
    # numbers that are less than or equal
    # to the argument integer.

def main():
    # Input a non-negative integer, n. Output
    # the Fibonacci numbers that are less than
    # or equal to that number, in order. If the
    # input is not a valid non-negative integer,
    # output a warning message.

The main function must input a string.
If the string does not represent a non-negative integer, then it should print a warning message.
If it does represent a non-negative integer, then it should call the fibonacci function to create
the list of Fibonacci numbers that are less than or equal to the non-negative integer and output this list.
The fibonacci function should call the append_fibonacci function multiple times to create the Fibonacci list. 

You must write a main program to test your functions but do not submit your main program.
Just copy and paste your three function definitions into the code box below.

Here are some sample runs of a main program that just calls the main function.

Enter a non-negative integer >23
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13, 21]

Enter a non-negative integer >13
The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13]

Enter a non-negative integer >0
The Fibonacci series starts with: []

Enter a non-negative integer >ten
ten is not a non-negative integer
'''

def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        integer_list.append(1)
    else:
        last1_fib = integer_list[-1]
        last2_fib = integer_list[-2]
        integer_list.append(last1_fib + last2_fib)

def fibonacci(max):
    fib_list = []
    append_fibonacci(fib_list)

    while fib_list[-1] <= max:
        append_fibonacci(fib_list)

    fib_list.remove(fib_list[-1])
    return fib_list

def main():
    usr_input = input('Enter a non-negative integer >')
    if usr_input.isdigit():
        fib_list = fibonacci(int(usr_input))
        print(f'The Fibonacci series starts with: {fib_list}')
    else:
        print(f'{usr_input} is not a non-negative integer')

main()