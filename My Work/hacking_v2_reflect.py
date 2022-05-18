from uagame import Window
from time import sleep

# Write a program that uses the uagame module to open a 300 by 200 pixel window with title, hello. 
window = Window('hello', 300, 200)

# Prompt the user to enter a string using the prompt string 'Enter string >'. The prompt must be in the top left corner of the window. 
str_prompt = window.input_string('Enter string >', 0, 0)

# Then, display the input string in the bottom right hand corner of  the window. 
# This program must work for any reasonable font size, so your program must use the Window methods named: 
# get_width, get_string_width, get_height, and get_font_height to compute the display_string coordinates for 
# displaying the string in the bottom right corner. 
x = window.get_width() - window.get_string_width(str_prompt)
y = window.get_height() - window.get_font_height()
window.draw_string(str_prompt, x, y)
window.update()

# The program should pause for 2 seconds after the string appears in the window and then the window should close.
sleep(2)
window.close()

# Your program must not input or display any other information.

