''' Write a Python program that asks the user to input a string that has an e as the middle character. 
If the string has an odd number of characters and an e as the middle character, 
output a positive message, as shown in the samples. 
If the string has an even number of characters or has an odd number of characters, 
but the middle character is not an e,  output the appropriate negative message as shown in the samples. '''

# sample 1
'''
Enter a string with an e in the middle >alberta
Yes, alberta has e in the middle, at index 3
'''

# sample 2
'''
Enter a string with an e in the middle >edmontonian
No, edmontonian has t in the middle, at index 5
'''

# sample 3
'''
Enter a string with an e in the middle >keep
No, keep has no middle character
'''


str_input = input("Enter a string with an e in the middle >")

# the string has an odd number of characters
str_len = len(str_input)
is_odd = str_len % 2 == 1
if is_odd:
    # and an 'e' as the middle character
    mid_index = (str_len) // 2
    mid_char_is_e = str_input[mid_index] == 'e'
    if mid_char_is_e:
        print(f"Yes, {str_input} has e in the middle, at index {mid_index}")
    else:
        print(f"No, {str_input} has {str_input[mid_index]} in the middle, at index {mid_index}")
else:
    print(f"No, {str_input} has no middle character")