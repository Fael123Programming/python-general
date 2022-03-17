def print_dict(a_dict: dict):
    for key, value in a_dict.items():
        print(f"{key} {value}")


if __name__ == "__main__":
    words = ["cat", "window", "defenestrate"]
    for w in words:
        print(w, len(w))
    print()
    users = {"Hans": "active", "Eleonore": "inactive", "Eric": "active", "Marcos": "inactive"}
    for user, status in users.copy().items():  # Modify a collection you should use a copy of it.
        if status == "inactive":
            del users[user]
    active_users = {}
    for user, status in users.items():
        if status == "active":
            active_users[user] = "active"
    print_dict(active_users)
    for i in range(101):
        print(i, end=" ")
    print("A range is not a list but a representation of a sequence of numbers. It is an iterable object.")
    print(sum([1, 2, 3]))  # Sum is a built-in function that takes an iterable as argument.
    print(sum(range(4)))
