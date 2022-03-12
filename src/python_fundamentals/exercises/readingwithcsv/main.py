import csv
from employee import Employee
from employees import Employees


def print_list(a_list: Employees):
    print("[", end="")
    for element in a_list:
        print(element, end="")
        if element != a_list[-1]:
            print(end="; ")
    print("]")


if __name__ == "__main__":
    with open("employees.txt") as file:
        reader = csv.reader(file)
        employees = Employees()
        for line in reader:
            e = Employee(line[0], line[1], float(line[2]))
            employees.append(e)
        print(f"There are {len(employees)} employees")
        # print_list(employees)
        print("Salaries: $")
        for e in employees:
            print(e.salary)
