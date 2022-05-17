# Hacking Version 2
# This is a text-based password guessing game that displays a 
# list of potential computer passwords. The player is allowed 
# 1 attempt to guess the password. The game indicates that the 
# player failed to guess the password correctly.

from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

# display header
line_y = 0
string_height = window.get_font_height()
window.draw_string('DEBUG MODE', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('1 ATTEMPT(S) LEFT', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# display password list
window.draw_string('PROVIDE', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('SETTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('CANTINA', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('CUTTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('HUNTERS', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('SURVIVE', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('HEARING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('HUNTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('REALIZE', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('NOTHING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('OVERLAP', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('FINDING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
window.draw_string('PUTTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# prompt for guess
guess = window.input_string('ENTER PASSWORD >', 0, line_y)
    
# end game
#   clear window
window.clear()
#   display failure outcome
#     display guess
#       compute x coordinate
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2

#       compute y coordinate
outcome_height = 7 * string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

window.draw_string(guess, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#     display blank line
window.draw_string('', line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#     display failure line 2
#       compute x coordinate
str_failure_outcome = 'LOGIN FAILURE - TERMINAL LOCKED'
x_space = window.get_width() - window.get_string_width(str_failure_outcome)
line_x = x_space // 2
window.draw_string(str_failure_outcome, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#     display blank line 
window.draw_string('', line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#     display failure line 3
#       compute x coordinate
str_failure_outcome = 'PLEASE CONTACT AN ADMINISTRATOR'
x_space = window.get_width() - window.get_string_width(str_failure_outcome)
line_x = x_space // 2
window.draw_string(str_failure_outcome, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#     display blank line 
window.draw_string('', line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#   prompt for end
str_failure_outcome = 'PRESS ENTER TO EXIT'
x_space = window.get_width() - window.get_string_width(str_failure_outcome)
line_x = x_space // 2
end_prompt = window.input_string(str_failure_outcome, line_x, line_y)

# close window
window.close