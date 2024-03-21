
alphabet = 'abcdefghijklmnopqrstuvwxyz., ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letter_then_index = dict(zip(alphabet, range(len(alphabet))))
index_then_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt (message, key):

    """Encodes the message by using the key to index each character."""

    encrypted = ''
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    #convert message to index and add the key
    for each_split in split_message:
        q = 0
        for letter in each_split:
            number = (letter_then_index[letter] + letter_then_index[key[q]]) % len(alphabet)
            encrypted += index_then_letter[number]
            q +=1

    # write encrpted message text

    return encrypted

def decrypt(cipher, key):

    """Decodes the cipher using the key"""
    decrypted = ''

    # split the cipher to the length of the key
    split_cipher = [cipher [k:k + len(key)] for k in range(0, len(cipher), len(key))]
    for each_split in split_cipher:
        j = 0
        for letter in each_split:
            number = (letter_then_index[letter] - letter_then_index[key[j]]) % len(alphabet)
            decrypted += index_then_letter[number]
            j += 1


    # write decrypted message text

    return decrypted

def main():

    """Main Program to run the program so the user may interact with it."""

    key = 'pineappleavocado'
    message = input("Enter message to be encryped: ")
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print('Original Message: ' + message)
    print('Encrypted Message: ' + encrypted_message)
    print('Decrypted Message: ' + decrypted_message)

main()

