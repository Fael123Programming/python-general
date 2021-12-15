# When you want to open() a resource and also, want it to close automatically
# you may use the 'with' command.
# There goes an example:
with open("python_fundamentals/language_syntax/with/tests.py") as file:
    print("-" * 100)
    for line in file:
        line = line.strip()  
        # Get blank spaces and new line escape characters from both bounds of a string (leading and trailing).
        # A bit similar to trim() from Java. 
        print(line)
    print("-" * 100)
print("\u2796")
# with is quite similar to try with resources in Java.