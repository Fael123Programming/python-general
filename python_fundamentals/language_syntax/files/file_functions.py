# file = open("python_fundamentals/language_syntax/files/test_file.txt", "w")
# open(file_path, mode)
# To only read a file, use as mode "r".
# To write onto it (override its info), use "w".
# To only append info, use "a".
# print(file.read()) -> read the whole info of the file putting the cursor at the end of it.
# If you want to read again, you have to open once again.
# print(file.readline(10)) -> read the first 10 characters of the file.
# If you do not pass a number into it, there will be considered the whole line.
# file.write(text) -> write a text into your file according to the mode you chose.
# Trying to open a file not using a mode explicitly, will use as default "r" which does
# not create a new file if it is not already created. To do that, you have to open it
# using "w".
# file.write("New information to this file.")
# file.write("Just go mindful...")
# Never forget to close() the stream you have created with open().
# file.close()
# file = open("python_fundamentals/language_syntax/files/test_file.txt", "a")
# file.write("\nNot overriding the information but adding new data...\n")
# file.write("Do not let slip your mind that you have got to use '\\n' to break rows...\n")
# file.close()
# We have opened files till now in the text mode but you can do that in the binary mode (like images, for example).
# image = open("C:/Users/rafae/OneDrive/Pictures/ruby.jpg", "rb")  # read in binary mode.
# print(image.read())
# image.close()
# Reading line per line using a for loop.
# line_per_line = open("C:/Users/rafae/OneDrive/Pictures/ruby.jpg", "rb")
# for line in line_per_line:
#    print(line)
# line_per_line.close()    
# Using the builtin readline
# a_file = open(file_path_you_chose, mode_of_opening)
# a_file.readline()
# a_file = open("python_fundamentals/language_syntax/files/test_file.txt")
# print(a_file.readline())
# a_file.close()
# a_file = open("python_fundamentals/language_syntax/files/test_file.txt")
# print(a_file.readlines()[4]) -> It grabs all lines and casts it into a list accessible through indexes.
# a_file.close()
# Use the 'with' command to automatically open and close a file:
# with open(file_path, mode) as file:
#     do_something()    