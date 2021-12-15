n = int(input("Number: "))
dividers = list()
for c in range(1,n + 1):
    if n % c == 0: dividers.append(c)
print(f"{n} has {len(dividers)} divider(s) and they are: {dividers} ")