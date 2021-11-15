# Dictionaries are another unordered data structure in Python. They are a collection of couples of keys and values like
# a map in another languages. Each map must be a string and the value can be whichever data type supported by Python.
# Constraints: there cannot be put a mutable data type (like a list) as a dictionary key and also, keys that is being used
# more than once.

def print_dict(dic: dict):
    for key, value in dic.items():
        print(key,":", value)


customer = {}
customer.update({"name": "Jorge Wilhelm"})
print(customer)
customer.update({"age": 40, "civil status": "single", "id": 1290934123})
print(customer)
print(customer.keys())
print(customer.values())
print_dict(customer)
customer["country"] = "England"
print()
print_dict(customer)
customer[(1, 2, 3)] = "Strange key, not?"
print(customer[(1, 2, 3)])
car = dict(color="Blue", trademark="BMW", value="500000", model="M8 Gran Coupé Competition")
print(car)
