alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
def caesar(caesar_text, shift_amount, direction_text):
    text_list = list(text)
    processed_text_list = []
    if direction_text == "decode":
        shift_amount *= -1
    for char in text_list:
        if char in alphabet:
            letter_index = alphabet.index(char)
            processed_text_list.append(alphabet[letter_index + shift_amount])
        else:
            processed_text_list.append(char)
    processed_text = ''.join(processed_text_list)
    print(f"The {direction}d text is {processed_text}")

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

quit_caesar = False
while not quit_caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(caesar_text=text, shift_amount=shift, direction_text=direction)
    continue_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()

    if continue_input == "yes":
        quit_caesar = False
    elif continue_input == "no":
        quit_caesar = True
        print("Goodbye")
