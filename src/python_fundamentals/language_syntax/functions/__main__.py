def get_standardized(a_person: dict, id=None):
    # 'id' is an optional argument!
    # 'a_person' is not!
    data = "Name: " + str(a_person["name"]) + "\nAge: " + str(a_person["age"]) + "\nNationality: " + str(
        a_person["nationality"]) + "\nId: "
    if id is not None:  # 'is' compares object references! 
        data += str(id)
    else:
        data += "<unknown>"
    return data


a_girl = {"name": "Britney", "age": 19, "nationality": "brazilian"}


def vel(space: float, time: float):  # 'space' in meters and 'time' in seconds. Then, 'vel' is in m/s.
    return space / time


def accel(space: float, time: float):
    return vel(space, time ** 2)


def calculator(n1, n2):
    return dict(sum=n1 + n2, sub=n1 - n2, mult=n1 * n2, div=n1 / n2, pow=n1 ** n2)


def sum_sub(n1, n2):
    return n1 + n2, n1 - n2


def sum_sub2(n1, n2):
    return {"sum": n1 + n2, "sub": n1 - n2}


print(sum_sub(10, 5))
print(sum_sub2(10, 5))
print(get_standardized(a_girl))
print("-" * 30)
print(get_standardized(a_girl, id=234))
print(accel(50000, 10))
print(vel(50000, 10) / 10)
print(vel(-20, 10))
# print(vel(150, 0)) ZeroDivisionError raised!!!
print("-" * 30)
result_obj = calculator(10, 5)
for key in result_obj:  # Another way to run through a dictionary!
    print(f"{key}: {result_obj[key]}")


# Magical variables: used with def's to allow you pass multiple parameters to a function.
# *args: multiple values.
# **kwargs: multiple couple of keys and values.
# The programmer does not know how many arguments will be passed to this function.

def sum(*args):
    result = 0
    for n in args:
        result += n
    return result


def show_args(*args):
    return args  # This is a tuple; your data is package into it.


print("Sum from 1 to 10 is " + str(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(sum(90, -50, 60))
print(show_args("name", 89, True, 12.22))
listOfNumbers = list(range(-10, 11))
print(show_args(listOfNumbers))  # listOfNumbers is considered as the first argument of the tuple args.
print(show_args(
    *listOfNumbers))  # Each element in listOfNumbers is considered as one argument passed to the function call.
print(sum(*range(1, 101)))


# '*' to package your data.
# The function is able to unpackage it.

def report(**kwargs) -> str:
    text = ""
    for key, value in kwargs.items():
        text += f"{key}: {value}\n"
    return text


def rep(**kwargs):
    return kwargs  # This is a dictionary; your data is package into it.


print(report(name="Rafael Fonseca", date_of_birth="06-11-2002", country="Brazil", profession="Student/Programmer"))
print(rep(name="Rafael Fonseca", date_of_birth="06-11-2002", country="Brazil", profession="Student/Programmer"))
a_person = {"name": "Mariana Silva", "country": "USA"}
print(report(
    **a_person))  # This dict will be unpackage and its couples of keyword-value will be passed to this function as we did above.


# print(report(a_person))  # Invalid usage.
# *args expects a tuple while **args expects a dictionary.

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: " + str(arg1))
    print("arg2: " + str(arg2))
    print("arg3: " + str(arg3))


arguments = (10, 45.78, "Python")
test_args_kwargs(*arguments)  # arguments is unpackage.
arguments2 = {"arg3": "Python", "arg1": 10, "arg2": 45.78}
print("-" * 50)
test_args_kwargs(**arguments2)
# arguments2 is also unpackage and each key is associated with each parameter at the signature of the function.
nums = (1, 2, 3, 4)
numsDict = {"arg1": 1, "arg2": 2, "arg3": 3, "arg4": 4}


# test_args_kwargs(*nums)  # unpackage this tuple! This raises an error though.
# test_args_kwargs(**numsDict)  # unpackage this dictionary! This raises an error though.


def calc(**kwargs):
    return kwargs["number1"] / kwargs["number2"]


print(calc(name="Rafael", state="on", number1=100, maximum_size=300,
           number2=50))  # This is random set of key-value couples.
