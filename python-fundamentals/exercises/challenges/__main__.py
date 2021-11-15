def greatest(a_list: list):
    def choose(n1: int, n2: int) -> int:
        return n1 if n1 > n2 else n2


    def gr(another_list: list, size_of_it: int) -> int:
        return another_list[0] if size_of_it == 1 else choose(another_list[size_of_it - 1], gr(another_list, size_of_it - 1))


    return gr(a_list, len(a_list))


def smallest(a_list: list):
    def choose(n1: int, n2: int) -> int:
        return n1 if n1 < n2 else n2


    def gr(another_list: list, size_of_it: int) -> int:
        return another_list[0] if size_of_it == 1 else choose(another_list[size_of_it - 1], gr(another_list, size_of_it - 1))


    return gr(a_list, len(a_list))


def even(a_list: list) -> list:
    even_numbers = []
    for number in a_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def mean(a_list: list):
    sum = 0
    for number in a_list:
        sum += number
    return sum / len(a_list)


def sum_negative(a_list: list):
    sum = 0
    for number in a_list:
        if number < 0:
            sum += number
    return sum 


list_of_numbers = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(greatest(list_of_numbers))
print(smallest(list_of_numbers))
print(even(list_of_numbers))
print(list_of_numbers.count(list_of_numbers[0]))
print(mean(list_of_numbers))
print(sum_negative(list_of_numbers))