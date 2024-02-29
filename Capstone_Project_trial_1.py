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

#def caesar_cipher("")


letters = 'abcdefghijklmnopqrstuvwxyz, .ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
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
print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print('Encryption Mode Selected')
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print (f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('Decryption Mode Selected')
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print (f'PLAINTEXT: {plaintext}')






