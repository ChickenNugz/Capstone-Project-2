# Cipher Encoder/Decoder
Included are 2 ciphers used for encoding and decoding messages. The first file utilizes a monoalphabetic cipher, the Caesar Cipher, and the second implements a polyalphabetic cipher, the Vigenere Cipher. 

With each cipher, once you run the program it will prompt the user for input. After receiving the input, the program will then encode or decode the message (depending on user input).

The Caesar cipher is a simple cipher that uses a single substition pattern to encode/decode a message. The user inputs a positive integer as the Key and the key will move each letter that many spaces down the database. In this case, the database is the variable at the beginning of the program. If the integer is larger than the amount of characters in the database, then it will loop back to the beginning of the database and keep counting forward. To decode a message that has been encoded this way, the user needs to input the same key that was used for encoding, and it will reverse the process.

The Vigenere Cipher is a polyalphabetic cipher and uses a double substition pattern to encode/decode the message. The user will input a string of characters as the key. This key will be used as a rotating encoder, ensuring that each character encoded with it will be random, making it difficult to crack without access to the key. 
