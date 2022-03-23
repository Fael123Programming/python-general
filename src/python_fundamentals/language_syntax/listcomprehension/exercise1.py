import math

if __name__ == "__main__":
    squares = list(map(lambda x: x ** 2, range(1, 11)))
    print(squares)
    squares2 = [x ** 2 for x in range(1, 11)]
    print(squares2)
    couples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(couples)
    vec = [-4, -2, 0, 2, 4]
    print([x * 2 for x in vec])
    print([x for x in vec if x >= 0])
    print([abs(x) for x in vec])
    fresh_fruits = ["  banana", "apple    ", "   pear    ", "   pineapple       "]
    print([fruit.strip() for fruit in fresh_fruits])
    print([(x, x ** 2) for x in range(1, 11)])
    a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    print([x for sublist in a_list for x in sublist])
    print([str(round(math.pi, i)) for i in range(1, 11)])
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print([[row[i] for row in matrix] for i in range(4)])
    print(list(zip(*matrix)))
