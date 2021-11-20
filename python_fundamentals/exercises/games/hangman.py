from time import sleep


def msg(text):
    print("-" * 50)
    print(text.center(50))
    print("-" * 50)


def print_list(a_list):
    for item in a_list:
        print(item, end="")


def invalidLetter(letter):
    if len(letter) > 1 or len(letter) == 0 or letter.isspace():
        return True
    from string import ascii_letters
    return not ascii_letters.__contains__(letter)


def clean_prompt():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def draw_gallows(quantity_of_errors):
    if quantity_of_errors == 0:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")  # Unicode character minus.
        print("|           |")
        print("|")
        print("|")
        print("|")
    elif quantity_of_errors == 1:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")
        print("|           |")
        print("|         ",u"\U0001F635")  # Unicode character face with crossed-out eyes.
        print("|")
        print("|")
    elif quantity_of_errors == 2:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")
        print("|           |")
        print("|         ",u"\U0001F635")
        print("|          \\")
        print("|")
    elif quantity_of_errors == 3:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")
        print("|           |")
        print("|         ",u"\U0001F635")
        print("|          \\/")
        print("|")
    elif quantity_of_errors == 4:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")
        print("|           |")
        print("|         ",u"\U0001F635")
        print("|          \\/")
        print("|          /")
    else:
        print("\u2796\u2796\u2796\u2796\u2796\u2796")
        print("|           |")
        print("|         ",u"\U0001F635")
        print("|          \\/")
        print("|          /\\")


def play(word, hint):
    won = False
    secret_word = {"word": word.lower(), "hint": hint.lower()}
    letters = list("*" * len(secret_word["word"])) # or you can code: ["*" for letter in secret_word["word"]]
    # Keep in mind that all strings are iterable.
    errors, counter = 0, 0
    msg("Hangman Game".center(50))
    print("Secret word: ", end="")
    print_list(letters)
    print("\nErrors:", errors)
    print("Hint:", secret_word["hint"])
    draw_gallows(errors)
    while True:
        letter = input("Letter of your choice: ").lower()
        clean_prompt()
        if invalidLetter(letter):
            msg("Not a letter")
            sleep(1)
        elif letter in secret_word["word"] and not letter in letters:  # 'not letter in letters' checks if the letter guessed is repeated.
            for l in secret_word["word"]:
                if letter == l:
                    letters[counter] = letter
                counter += 1
            counter = 0
        else:
            msg(f"{letter} was not found.")
            errors += 1
            sleep(1)
        clean_prompt()
        if "*" not in letters or errors == 5:
            # If the player has found all hidden letters, 'won' will be assigned with True.
            # Otherwise, with False... he lose it (errors == 5) is True).
            won = "*" not in letters
            break
        msg("Hangman Game".center(50))
        print("Secret word: ", end="")
        print_list(letters)
        print("\nErrors:", errors)
        print("Hint:", secret_word["hint"])
        draw_gallows(errors)
    if won:
        msg("You got it... congratulations!!!")
        print(u"\U0001F3C6")  # Unicode character trophy. 
    else:
        msg("Unfortunately, you did not reach that...") 
        print(u"\U0001F480")  # Unicode character skull.  
        draw_gallows(errors)
    print("The word is", secret_word["word"]) 
    sleep(2)
    clean_prompt()   
