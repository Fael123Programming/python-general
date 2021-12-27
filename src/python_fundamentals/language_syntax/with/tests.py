# When you want to open() a resource and also, want it to close automatically
# you may use the 'with' command.
# There goes an example:
if __name__ == "__main__":
    with open("C:/Users/rafae/OneDrive/Documents/prg/py/src/on-data/ex01.py") as file:
        print("-" * 100)
        for line in file:
            line = line.strip()
            # Get blank spaces and new line escape characters from both bounds of a string (leading and trailing).
            # A bit similar to trim() from Java.
            print(line)
        print("-" * 100)
    print("\u2796")
    # with is quite similar to try-with-resources in Java.
