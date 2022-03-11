import csv
from employee import Employee

if __name__ == "__main__":
    with open("employees.txt") as file:
        reader = csv.reader(file)
        employees = list()
        for line in reader:
            print(line)
            employees.append(Employee(line[0], line[1], float(line[2])))
        print(employees)
