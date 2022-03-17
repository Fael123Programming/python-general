from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


if __name__ == "__main__":
    try:
        color = Color(input("Enter your choice of 'red', 'blue' or 'green': ").lower().strip())
    except ValueError:
        print(f"Color not recognized")
    else:
        match color:
            case Color.RED:
                print("Red was chosen...")
            case Color.BLUE:
                print("Blue was chosen...")
            case Color.GREEN:
                print("Green was chosen...")
