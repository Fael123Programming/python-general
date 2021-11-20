from root_file import root_file
from file_handler import record_in_file

newWord = input("New word: ")
hint = input("Hint for it: ")
print("-" * 60)
record_in_file(newWord, hint, root_file)
print("Added succesfully!")
