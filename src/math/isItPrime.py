n = int(input("Number: "))
if n == 0 or n == 1 or n < 0: print("Not prime by definition")
else:
    dividers = 0
    for counter in range(1,n + 1): 
        if n % counter == 0: dividers += 1
    print(f"{n} is prime") if dividers == 2 else print(f"{n} is not prime")
