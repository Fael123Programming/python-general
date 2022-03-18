def test1(arg1, *a_tuple, **a_dict):
    print("Single arg: " + arg1)
    print("Multiple data passed as argument: " + str(a_tuple))
    print("-------------------------------------------------------------------------")
    for kw in a_dict:
        print(kw, ":", a_dict[kw])


def summation(*numbers):
    result = 0
    for value in numbers:
        result += value
    # print(numbers.__class__.__name__)
    return result


def pos_only_arg(arg, /):  # Only one positional argument is accepted.
    print(arg)


def kwd_only_arg(*, arg):  # Only one keyword argument (named argument) is accepted.
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def foo(name, /, **kwds):
    return 'name' in kwds


def concat(*args, sep="/"):
    return sep.join(args)


def receive_dict_data(name, age):
    print(name, "has", age, "years old.")


def receive_list_data(start, end):
    for c in range(start, end):
        print(c)


if __name__ == "__main__":
    test1("Any string", 1, 2, 3, "Bla bla bla", True, 1.567, price=4.5, brand="Nike", country="Brazil")
    print(summation(1, 2, 3, 4, 5, 10129312309, 123123))
    pos_only_arg(123)
    # pos_only_arg(arg=123) -> Cannot be done.
    kwd_only_arg(arg=123)
    # kwd_only_arg(123) -> Cannot be done.
    combined_example(123, 456, kwd_only="string")
#     There are positional arguments and keyword (named) arguments.
    print(foo(123, name=90, today="wednesday"))
    print(concat("home", "dev", "java", "project"))
    print(concat("https://www", "youtube", "com", sep="."))
    person = {"name": "Rafael Fonseca", "age": 19}
    receive_dict_data(**person)  # Unpacking a dict into its key-value pairs.
    pair_of_values = [1, 11]
    receive_list_data(*pair_of_values)  # Unpacking a list into its members.
