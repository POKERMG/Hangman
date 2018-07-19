
# Hangman for Python 3.6 - Developed by MG

# Defining the word for HangMan
def hangman(word):
    # Initial Wrong Starting at Zero
    wrong = 0
    # Setup of Hang-Man Graphic
    hangs = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               ",
              "|               "
              ]
    wordLetters = list(word)
    # Setup of Graphic for word
    boardGame = ["__"] * len(word)
    # Setup of win is set to False at start
    win = False
    # Additional space below
    print("\n")
    # Welcome Message
    print("Welcome to the Python Version of HangMan - Made by MG")
    # If letter is guessed wrongly then hangs is -1
    while wrong < len(hangs) - 1:
        # Spaces for graphic
        print("\n")
        print("\n")
        print("\n")
        # Guess a letter
        message = "Please guess a letter : "
        # Input of Character
        characters = input(message)
        # if the character is correct then relate to work
        if characters in wordLetters:
            wordBinder = wordLetters \
                .index(characters)
            boardGame[wordBinder] = characters
            wordLetters[wordBinder] = '$'
        # Otherwise if wrong add to total count of wrong
        else:
            wrong += 1
        # print the amount of letters
        print((" ".join(boardGame)))
        e = wrong + 1
        print("\n"
              .join(hangs[0: e]))
        # if there are no '__' left then you win as you found the correct word
        if "__" not in boardGame:
            print("Well done You win!")
            print(" ".join(boardGame))
            win = Trueg
            break
        # if not then you lose - as you have been hanged
    if not win:
        print("\n"
              .join(hangs[0: \
                           wrong]))
        print("You lose! The word was {}."
              .format(word))

# Current Guess Word
hangman("notify")