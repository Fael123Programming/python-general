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

won, hung = False, False
secret_word = {"word": "jesus", "hint": "A famous person on history"}
letters = list("*" * len(secret_word["word"]))
errors, counter = 0, 0
msg("Hangman Game".center(50))
print("Secret word: ", end="")
print_list(letters)
print("\nErrors:", errors)
print("Hint:", secret_word["hint"])
while True:
    letter = input("Letter of your choice: ")
    clean_prompt()
    if invalidLetter(letter):
        msg("Not a letter")
        sleep(1)
    elif letter in secret_word["word"] and not letter in letters:
        for l in secret_word["word"]:
            if letter.upper() == l.upper():
                letters[counter] = letter
            counter += 1
        counter = 0        
    else:
        msg(f"{letter} was not found in {secret_word['word']}.")
        errors += 1
        sleep(1)
    clean_prompt()
    if "*" not in letters or errors == len(secret_word["word"]):
        won = "*" not in letters
        hung = errors == len(secret_word["word"])
        break
    msg("Hangman Game".center(50))
    print("Secret word: ", end="")
    print_list(letters)
    print("\nErrors:", errors)
    print("Hint:", secret_word["hint"])
if won:
    msg("You got it... Congratulations!!!")
    print("The word is", secret_word["word"])
else:
    msg("Unfortunately, you did not reach that...")
