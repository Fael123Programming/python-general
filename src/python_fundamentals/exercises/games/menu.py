import divination
import hangman
import file_handler
from root_file import root_file

# You can import external files and access their features 
# like functions, classes and moreover. They are accessed like
# objects, that is, using a dot.
# If we do type(divination) or type(hangman), there will be shown <class 'module'>.
# Everything in Python are objects even though a file.
# print(type(divination))
# print(type(hangman))

file_handler.create_local_file(root_file)

while True:
    hangman.msg("Menu of Games")
    print("1. Divination")
    print("2. Hangman")
    print("3. Exit")
    print("-" * 50)
    choice = input("-> ")
    hangman.clean_prompt()
    if choice == "1":
        divination.play()
    elif choice == "2":
        hangman.play(*file_handler.choose_word_to_play_randomly(root_file))
        # It returns a tuple (packaged set of data). Then we use '*' to unpackage it
        # and to extract the two required arguments this function demands: a word
        # and a hint for it.
    elif choice == "3":
        exit(0)
    else:
        hangman.msg("Invalid choice")
        hangman.sleep(1)
        hangman.clean_prompt()