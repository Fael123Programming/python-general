class Divination:
    EASY, INTERMEDIATE, HARD = 1, 2, 3

    def __init__(self, number, mode):
        self.number = number
        if mode == Divination.EASY:
            self.chances = 20
        elif mode == Divination.INTERMEDIATE:
            self.chances = 10
        elif mode == Divination.HARD:
            self.chances = 5
        else:
            raise Exception("Unrecognized mode")

    def __str__(self) -> str:
        return "Divination object{{number={}, chances={}}}".format(self.number, self.chances)

    def start(self) -> None:
        from time import sleep

        def clean():
            import os
            os.system("cls" if os.name == "nt" else "clear")

        player_points = 1000
        while self.chances > 0:
            print("*" * 50)
            print("Divination Game".center(50))
            print("*" * 50)
            try:
                print("Points:", player_points)
                print("Chances:", self.chances)
                value = int(input("Guess a value: "))
                if value == self.number:
                    print("You got it!")
                    exit(0)
                elif value > self.number:
                    print("You entered a value greater than the target!")
                elif value < self.number:
                    print("You entered a value less than the target!")
                player_points -= abs(self.number - value)
                self.chances -= 1
            except ValueError:
                clean()
                print("Invalid value")
            finally:
                sleep(1)
                clean()
        print("Unfortunately, your chances have run out")

