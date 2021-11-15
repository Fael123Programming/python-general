def get_standardized(a_person: dict, id=None):
    # 'id' is an optional argument!
    # 'a_person' is not!
    data = "Name: " + str(a_person["name"]) + "\nAge: " + str(a_person["age"]) + "\nNationality: " + str(a_person["nationality"]) + "\nId: "
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
    return dict(sum=n1+n2, sub=n1-n2, mult=n1*n2, div=n1/n2, pow=n1**n2)

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