def get_name() -> str:
    name = input("Enter your name: ")

    def change_name():
        nonlocal name
        name += " (Verified)"

    if input("Is it verified? ")[0].lower() == 'y':
        change_name()
    return name


def greet(name: str) -> str:
    return f"Bonjour et bienvenue {name}!"


if __name__ == "__main__":
    # print(greet(get_name()))
    # a, *rest, b = range(1, 5)
    # print(a, rest, b, sep="  ")
    l = [1, "Never give up", True]
    l.extend((1, 2, 3))  # Insere novos elementos no final da lista!
    print(l)