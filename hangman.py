from random import randint
from os import path,system
import time
import pyfiglet
import draw_a_hangman as drawing

def pick_capital():
    '''
    Picks a random European capital
    Returns:
    str: The name of European capital
    '''
    dirpath = path.dirname(__file__)
    filename = "capital.txt"
    filepath = dirpath + '/' + filename

    capital_list = []
    
    with open('capital.txt', 'r') as read_capital:
        for line in read_capital:
            capital_list.append(line)
    draw_random_index = randint(0, len(capital_list)-1)
    capital_to_guess = str(capital_list[draw_random_index]).upper().strip()
    return capital_to_guess

def get_hashed(word):
    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.
    Args:
    str: The word to hash
    Returns:
    str: The hashed password
    '''
    hashed_password = ''
    for w in word:
        if w == ' ':
            hashed_password = hashed_password + '  '
        else:
            hashed_password = hashed_password + "_ "
    return hashed_password


def uncover(hashed_password, password, letter):
    '''
    Uncovers all occurences of the given letter in the hashed password based on the password
    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover
    Returns:
    str: The hashed password with uncovered letter
    '''
    if len(letter) == 1:
        uncovered_hashed_password_list = list(hashed_password)
        for index, char in enumerate(password):
            if char == letter:
                uncovered_hashed_password_list[index * 2] = letter
        uncovered_hashed_password = ''.join(uncovered_hashed_password_list)
        return uncovered_hashed_password
    elif len(letter) == len(password):
        return letter
    else:
        return hashed_password
   


def update(used_letters, letter):
    '''
    Appends the letter to used_letters if it doesn't occur
    Args:
    list: The list of already used letters
    str: The letter to append
    Returns:
    list: The updated list of already used letters
    # '''
    if len(letter) == 1:
        if letter not in used_letters:
            used_letters.append(letter)
            return used_letters
        else:
            print('This letter is already used!')
            return used_letters
    else:
        return used_letters
 

def is_win(uncovered_hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered
    Args:
    str: The hashed password
    str: The password
    Returns:
    bool:
    '''
    no_whitespace_password = ''
    for letter in uncovered_hashed_password:
        if(letter.isalpha()):
            no_whitespace_password += letter

    if(no_whitespace_password == password):
        print(pyfiglet.figlet_format('You win'))
        return True
    else:
        return False


def is_loose(life_points):
    '''
    Checks if life points is equal 0
    Args:
    int: The life life_points
    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    if life_points == 0:
        print(pyfiglet.figlet_format('You loose'))
        return True
    else:
        return False


def get_input():
    '''
    Reads a user input until it contains only letter
    Returns:
    str: The validated input
    '''
    user_input = input('Choose a letter: ').upper()
    letter = user_input.isalpha()

    while(letter == False):
        system('clear')
        print('Please input a letter')
        user_input = input('Choose a letter: ').upper()
        letter = user_input.isalpha()
    return user_input
    

def main():
    system('clear')
    life_points = 6
    used_letters = []
    print('WELCOME TO HANGMAN')
    print('guess a capitol')
    random_capital = pick_capital()
    print(random_capital)
    hashed_capitol = get_hashed(random_capital)
    print(hashed_capitol + '\n')
    uncovered_password = hashed_capitol
    stop_game = True

    while(stop_game != is_loose(life_points) and stop_game != is_win(uncovered_password,random_capital)):
        print("You have %d try" % life_points)
        print(drawing.draw_a_hangman()[life_points])
        user_input = get_input()
        if(user_input == random_capital):
            print(pyfiglet.figlet_format('You win'))
            break
        elif(len(user_input) == len(random_capital)):
            life_points -= 1
            continue
        if(user_input not in used_letters and user_input not in random_capital):
            life_points -= 1
        elif(len(user_input) > 1 and len(user_input) < len(random_capital) ):
            life_points -= 1
  
        system('clear')
        check_win = is_win(uncovered_password, user_input)
        used_letters = update(used_letters, user_input)
        uncovered_password = uncover(uncovered_password, random_capital, user_input)
        print(uncovered_password)
        print('Letters already used: ' + ' '.join(used_letters))
    print(drawing.draw_a_hangman()[life_points])

if __name__ == '__main__':
    main()
