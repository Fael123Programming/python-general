# Module with the responsibility to handle our files in our project of games.
# It defines and implements some handy functions to work with them seamlessly
# according to our needs. Then, they can or cannot be useful for your project
# depending on what you want to do.

def file_lines(path):
    try:
        with open(path) as file:  # Default reading mode.
            lines = 0
            for line in file:
                lines += 1
            return lines    
    except FileNotFoundError:
        return "File not found"
    # The following code is no longer needed.    
    """else:    
        lines = 0
        for line in file:
            lines += 1
        return lines
    finally:
        file.close()"""


def record_in_file(word, hint, path):
    with open(path, "a") as file:    
        if file_lines(path) == 0:
            file.write(word + ":" + hint)
        else:
            file.write("\n" + word + ":" + hint)    


def is_an_existing_file(path):
    from os.path import isfile
    return isfile(path)


def create_local_file(path):
    if is_an_existing_file(path):
        return
    with open(path, "w") as file:
        pass


"""def bring_words_and_hints(path):
    try:
        file = open(path, "r")
    except FileNotFoundError:
        return "File not found"
    else:        
        words_and_hints = list()
        for line in file:
            word, hint = line.split(":")[0].strip(), line.split(":")[1].strip()
            words_and_hints.append({"word": word, "hint": hint})
        file.close()
        return words_and_hints"""


def choose_word_to_play_randomly(path):
    from random import randrange
    # There is a slight difference between randrange() and randint(): the first deos not
    # include the ending number; the second does include it.
    try:
        with open(path, "r") as file:
            whole_str =  file.readlines()[randrange(0, file_lines(path))]
            return whole_str.split(":")[0].strip(), whole_str.split(":")[1].strip() 
            # Multiple return: a tuple with a word and hint for it.
    except FileNotFoundError:
        return "File not found"   
