# Hacking Version 6
# This is a graphical password guessing game that displays a 
# list of potential computer passwords. The player is allowed 
# up to 4 attempts to guess the password. Each time the user 
# guesses incorrectly, the user is prompted to make a new guess. 
# The game indicates whether the player successfully guessed 
# the password or not.

from uagame import Window
from time import sleep

def main():
    '''
    Main program execution.
    '''
    location = [0, 0]
    window = create_window()
    attempts_left = 4
    display_header(window, location, attempts_left)
    password = display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts_left)
    end_game(window, guess, password)

def create_window():
    ''' Create a new window object with customized properties '''
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window
    
def display_header(window, location, attempts):
    '''
    Display strings on the header. Also returns number of attempts left.
    - window is the Window to display in
    - location is a tuple containing the int x and int y coords of where the string should be displayed 
        and it should be updated to one "line" below the top left corner of the displayed string
    - attempts_left is the number of attempt(s) left
    '''
    attempts_left = 4
    header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']
    for header_line in header:
        display_line(window, header_line, location)

    return attempts_left

def display_line(window, string, location):
    '''
    Display a string in the window and update the location
    - window is the Window to display in
    - string is the str to display in
    - location is a tuple containing the int x and int y coords of where the string should be displayed 
        and it should be updated to one "line" below the top left corner of the displayed string
    '''
    pause_time = 0.3
    string_height = window.get_font_height()
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause_time)
    location[1] = location[1] + string_height

def display_password_list(window, location):
    '''
    Display all password in the list to the window. Also return the password.
    - window is the Window to display in
    - location is a tuple containing the int x and int y coords of where the string should be displayed 
        and it should be updated to one "line" below the top left corner of the displayed string 
    '''
    pause_time = 0.3
    string_height = window.get_font_height()
    #   create password list
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE',  'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for password in password_list:
        # display password line
        window.draw_string(password, location[0], location[1])
        window.update()
        sleep(pause_time)
        location[1] = location[1] + string_height
    
    return password_list[7]

def get_guesses(window, password, location, attempts_left):
    '''
    Get user guess, and check the password. Also, return the guess at the end.
    - window is the Window to display in
    - password is the correct password
    - location is a tuple containing the int x and int y coords of where the string should be displayed 
        and it should be updated to one "line" below the top left corner of the displayed string 
    - attempts_left is the number of attempt(s) left
    '''
    string_height = window.get_font_height()
    # get guesses
    prompt = 'ENTER PASSWORD >'
    #   prompt for guess
    guess = prompt_user(window, prompt, location)

    attempts_left = attempts_left - 1

    while guess != password and attempts_left > 0:
        # get next guess
        #   display attempts left
        window.draw_string(str(attempts_left), location[0], string_height)
        
        #   check warning
        check_warning(window, attempts_left)
                
        #   prompt for guess
        guess = prompt_user(window, prompt, location)

        attempts_left = attempts_left - 1

    return guess

def end_game(window, guess, password):
    '''
    Clear the window, create outcome, and close window.
    - window is the Window to display in
    - guess is the guess made by user
    - password is the correct password
    '''
    string_height = window.get_font_height()
    location = [0, 0]
    #   clear window
    window.clear()

    #   create outcome
    if guess == password:
        # create success
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        prompt = 'PRESS ENTER TO CONTINUE'
    else:
        # create failure
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '','PLEASE CONTACT AN ADMINISTRATOR', '']
        prompt = 'PRESS ENTER TO EXIT'
            
    #   display outcome 
    location = display_outcome(window, outcome)

    #   prompt for end
    location[0] = (window.get_width() - window.get_string_width(prompt)) // 2
    prompt_user(window, prompt, location)

    #   close window
    window.close()

def prompt_user(window, prompt, location):
    '''
    Prompts user for input. Also return the user input string.
    - window is the Window to display in
    - prompt is the message for the message prompt
    - location is a tuple containing the int x and int y coords of where the string should be displayed 
        and it should be updated to one "line" below the top left corner of the displayed string 
    '''
    string_height = window.get_font_height()
    #   prompt for something
    usr_input = window.input_string(prompt, location[0], location[1])
    location[1] = location[1] + string_height
    return usr_input
    
def check_warning(window, attempts_left):
    '''
    Check attempts left.
    - window is the Window to display in
    - attempts_left is the number of attempt(s) left
    '''
    string_height = window.get_font_height()
    if attempts_left == 1:
        # display warning
        warning_string = '*** LOCKOUT WARNING ***'
        warning_x = window.get_width() - window.get_string_width(warning_string)
        warning_y = window.get_height() - string_height
        window.draw_string(warning_string, warning_x, warning_y)

def display_outcome(window, outcome):
    '''
    - window is the Window to display in
    - outcome is the message displayed for the outcome
    '''
    string_height = window.get_font_height()
    location = [0, 0]
    #   display outcome 
    #      compute y coordinate
    outcome_height = (len(outcome) + 1) * string_height
    y_space = window.get_height() - outcome_height
    location[1] = y_space // 2

    for outcome_line in outcome:
        # display centered outcome line
        #    compute x coordinate
        x_space = window.get_width() - window.get_string_width(outcome_line)
        location[0] = x_space // 2

        display_line(window, outcome_line, location)
    
    return location

main()