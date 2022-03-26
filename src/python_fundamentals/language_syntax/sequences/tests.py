if __name__ == "__main__":
    empty = ()
    singleton = ("hello", )  # A tuple with only one value.
    print(len(empty))
    print(len(singleton))
    print(empty)
    print(singleton)
    t = 12345, 54321, "bom dia!"
    x, y, z = t  # Multiple assignment.
    print(x, y, z, sep=" ")
    a = [1, 2, 3, 4]
    p, q, r, s = a
    print(p, q, r, s, sep=" ")

