alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    plain_text_list = list(text)
    cipher_text_list = []
    for letter in plain_text_list:
        letter_index = alphabet.index(letter)
        if letter_index + shift >= 25:
            cipher_text_list.append(alphabet[letter_index + shift - 26])
        else:
            cipher_text_list.append(alphabet[letter_index + shift])
    cipher_text = ''.join(cipher_text_list)
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount_backwards):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    cipher_text_list = list(text)
    plain_text_list = []
    for letter in cipher_text_list:
        letter_index = alphabet.index(letter)
        plain_text_list.append(alphabet[letter_index - shift])

    plain_text = ''.join(plain_text_list)
    print(f"The decoded text is {plain_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount_backwards=shift)