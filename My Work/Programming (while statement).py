'''
Prompt the user to enter the Fibonacci numbers in order until the user either 
makes a mistake or enters the first Fibonacci number greater than 50. If the user makes an error, 
output a consolation message as shown in the sample run and end the program. 
If the user enters all of the Fibonacci numbers successfully then output a congratulations message 
as shown in the sample runs and end the program. Some people start the Fibonacci numbers and 0 and some people start at 1. 
In this question, we will start at 1:

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >2
Enter the next Fibonacci number >3
Enter the next Fibonacci number >5
Enter the next Fibonacci number >8
Enter the next Fibonacci number >13
Enter the next Fibonacci number >21
Enter the next Fibonacci number >34
Enter the next Fibonacci number >55
Well done

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >4
Try again

Enter the next Fibonacci number >1
Enter the next Fibonacci number >1
Enter the next Fibonacci number >2
Enter the next Fibonacci number >3
Enter the next Fibonacci number >5
Enter the next Fibonacci number >8
Enter the next Fibonacci number >13
Enter the next Fibonacci number >21
Enter the next Fibonacci number >34
Enter the next Fibonacci number >60
Try again
'''

fib_1before = 0
fib_2before = 0
usr_input = int(input("Enter the next Fibonacci number >"))
if usr_input == 1:
    fib_2before = fib_1before
    fib_1before = usr_input

    usr_input = int(input("Enter the next Fibonacci number >"))
    sum2_before = fib_1before + fib_2before
    while (usr_input == sum2_before) and (sum2_before <= 50):
        fib_2before = fib_1before
        fib_1before = usr_input

        usr_input = int(input("Enter the next Fibonacci number >"))
        sum2_before = fib_1before + fib_2before
    if (usr_input != sum2_before):
        print("Try again")
    else:
        print("Well done")
else:
    print("Try again")
