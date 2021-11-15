# Sets are unordered data structures that keep your data but it does not give you certainty of positioning
# of elements. Also, it does not permit doubled items. The only thing that matters is the idea of belonging.
# They support all mathematical operations with sets: union, intersection, difference and simetric difference.
def check_and_remove(a_set: set, item: object):
    if a_set.__contains__(item):
        a_set.remove(item)
        return item
    return None


a_set = {1, 2, 3, 4}
a_set.add("a fruit")
print(a_set.__contains__("a fruit"))  # This is what matters using sets.
a_set.remove("a fruit")
print(a_set)
another_set = set(range(1, 11))
print(another_set)
print(another_set, " - ", a_set, "=", (another_set - a_set))  # Difference: -
print(another_set, "U", a_set, "=", another_set | a_set)  # Union: |
print(another_set, "\u2229", a_set, "=", another_set & a_set)  # Intersection: &
print("Simetric difference between them:", another_set ^ a_set)  # Simetric difference: ^
jesus = set("jesus")
for c in range(10):
    print(jesus)
# To create an empty set, do not use {} but set().
# {} only creates an empty dictionary.
what_is_it = {}
print(type(what_is_it))
print(check_and_remove(a_set, 1))
print(a_set.__contains__(1))