MORSE_CODE_LEGEND = {"A": ".-",
                     "B": "	-...",
                     "C": "-.-.",
                     "D": "-..",
                     "E": ".",
                     "F": "..-.",
                     "G": "--.",
                     "H": "....",
                     "I": "..",
                     "J": ".---",
                     "K": "-.-",
                     "L": ".-..",
                     "M": "--",
                     "N": "-.",
                     "O": "---",
                     "P": ".--.",
                     "Q": "--.-",
                     "R": ".-.",
                     "S": "...",
                     "T": "-",
                     "U": "..-",
                     "V": "...-",
                     "W": ".--",
                     "X": "-..-",
                     "Y": "-.--",
                     "Z": "--..",
                     "0": "-----",
                     "1": ".----",
                     "2": "..---",
                     "3": "...--",
                     "4": "....-",
                     "5": ".....",
                     "6": "-....",
                     "7": "--...",
                     "8": "---..",
                     "9": "----.",
                     " ": "/"
                     }

key_list = list(MORSE_CODE_LEGEND.keys())
val_list = list(MORSE_CODE_LEGEND.values())

print("Hello & Welcome to the the text to Morse Code Generator")
ok = True
while ok:
    function = input("to translate from text to morse type '1' and to translate from morse to text type '2' & to terminate type '0'\n")

    if function == "1":
        user_input = input("Please type your text below (DONT USE SYMBOLS)\n")
        text = []
        for letter in user_input.upper():
            morse = MORSE_CODE_LEGEND[letter]
            text.append(morse)

        print(f"{user_input} in morse translates to: {' '.join(text)}")

    elif function == "2":
        user_input = input("Please type your morse code below\n")
        x = user_input.split()
        text = []
        for letter in x:
            position = val_list.index(letter)
            morse = key_list[position]
            # morse = {i for i in MORSE_CODE_LEGEND if MORSE_CODE_LEGEND[i] == letter}
            text.append(morse)
        print(f"{user_input} in morse translates to: {' '.join(text)}")

    elif function == "0":
        print("Good bye")
        ok = False

    else:
        print("please enter a valid argument")

