from random import randint

def pick_capital():
    '''
    Picks a random European capital
    Returns:
    str: The name of European capital
    '''
    capital_list = []
    
    with open('capital.txt', 'r') as read_capital:
        for line in read_capital:
            capital_list.append(line)
    draw_random_index = randint(0, len(capital_list)-1)
    capital_to_guess = str(capital_list[draw_random_index]).upper()
    return capital_to_guess

print(pick_capital())

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
        return 'Jesteś idiotą.'


def update(used_letters, letter):
    '''
    Appends the letter to used_letters if it doesn't occur
    Args:
    list: The list of already used letters
    str: The letter to append
    Returns:
    list: The updated list of already used letters
    '''
    if letter in used_letters:
        print('This letter is already used')
        return used_letters
    else:
        return used_letters.append(letter)
    pass


def is_win(uncovered_hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered
    Args:
    str: The hashed password
    str: The password
    Returns:
    bool:
    '''
    if(uncovered_hashed_password == password):
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
        return True
    else:
        return False


def get_input():
    '''
    Reads a user input until it contains only letter
    Returns:
    str: The validated input
    '''
    user_input = str(input('Choose a letter: ').upper())

    if user_input.isalpha():
        return user_input
    else:  
        return 'Please input a letter'

print(get_input())

def main():
    pass


if __name__ == '__main__':
    main()
