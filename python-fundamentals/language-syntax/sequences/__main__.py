# Sequences are data structures that can hold multiple types of data.
# In Python, they are: lists, tuples and ranges.
# They can mutable or immutable: only lists are mutable, that is, their elements can be modified and changed after 
# it has been created.
def printList(a_list):
    for item in a_list:
        print(item)


numbers_and_letters = [123, 89.923, "number list"]
print(numbers_and_letters)
print(type(numbers_and_letters))
taxes = (45.67, 13.45, 88.11)
print(taxes + taxes)  # Concatenation is valid with sequences!
taxes *= 2  # taxes is doubled...
print(taxes) 
print(taxes[len(taxes) - 1], taxes[-1])
name = ["J", "e", "s", "u", "s"]
print(name[0:len(name):2])
print(min(name))
print(max(name))
thousand_to_zero = range(1000, -1, -1)
print(min(thousand_to_zero))
print(max(thousand_to_zero))
print(thousand_to_zero.count(500))
new_list = list("12123")  # An iterable argument should be passed (numbers are not iterable though).
print(new_list)
another_list = list(range(1, 13))
print(another_list)
print(another_list[-8:])
names = []
names.append("Jesus")
names.append("Jesus")
names.extend(range(1, 10, 2))
print(names)
names.extend(["Never give up", 3.45])
names.extend(range(0, 10, 2))
print(names)
print(names + [10, 50, 100])
print(names)
printList(names)
myTuple = 1, 2, 3, "Jesus I cannot forget you notime"  # You decide if you will use parentheses!
print(type(myTuple))
sequence_of_numbers = tuple(["one", "thousand", "thirty-three"])
print(myTuple)
print(sequence_of_numbers)
inner_list = ["This item", "is mutable"]
tup1 = 1, "Markdown", 3.45, inner_list
print(tup1)
inner_list.clear()
inner_list.append("Did not I say it?")
print(tup1)