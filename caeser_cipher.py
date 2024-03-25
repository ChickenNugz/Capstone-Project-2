#First Trial run at capstone coding project
#Mono Alphabetic ciphers: Caesar Cipher
numbered_dict_of_letters = {
       1:"A",
       2:"B",
       3:"C",
       4:"D",
       5:"E",
       6:"F",
       7:"G",
       8:"H",
       9:"I",
       10:"J",
       11:"K",
       12:"L",
       13:"M",
       14:"N",
       15:"O",
       16:"P",
       17:"Q",
       18:"R",
       19:"S",
       20:"T",
       21:"U",
       22:"V",
       23:"W",
       24:"X",
       25:"Y",
       26:"Z"
       }

#test comment for pushing to github


letters = 'abcdefghij klmnopqrstuvwxyz,!@#.ABCDEFGHIJKLMNOPQRSTUVWXYZ$%^&*()_+=-`~[]{};:|<>?'
num_letters = len(letters)

def get_key():

    """Gets an appropriate key from user input"""

    try:
        key_input = int(input('Enter the key (1 through 90): '))
        if key_input > 90 or key_input < 1:
            raise ValueError('Invalid response. Please enter a number between 1 and 90')
        return key_input
    except ValueError as e:
        print(e)
        return get_key()


def encrypt_decrypt(text, mode, key):

    """Function to be used to decrypt or encrypt the message depending on user input. Uses the key"""

    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


print('\n','***CAESAR CIPHER PROGRAM***', '\n')
def get_user_input():

    """Asks the user if they want to encrypt or decrypt, and raises an error if they submit invalid input."""

    try:
        user_input = input('Do you want to encrypt or decrypt? Valid responses: "e" OR "d": ').lower()
        if user_input != 'e' and user_input != 'd':
            raise ValueError('Invalid response. Please type "e" or "d"')
        return user_input
    except ValueError as e:
        print(e)
        return get_user_input()


def run_program():
    user_input = get_user_input()

    if user_input == 'e':
        print('Encryption Mode Selected')
        key = get_key()
        text = input('Enter the text to encrypt: ')
        ciphertext = encrypt_decrypt(text, user_input, key)
        print (f'CIPHERTEXT: "{ciphertext}"')

    elif user_input == 'd':
        print('Decryption Mode Selected')
        key = int(input('Enter the key (1 through 90): '))
        text = input('Enter the text to decrypt: ')
        plaintext = encrypt_decrypt(text, user_input, key)
        print (f'PLAINTEXT: "{plaintext}"')

    run_program()

run_program()

