from uagame import Window
from time import sleep

window = Window('hello', 300, 200)
print(type(window.input_string('Enter a word >', 0, 0)))