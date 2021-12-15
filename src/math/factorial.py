def fact(n):
    res = 1
    for counter in range(2, n + 1):
        res *= counter
    return res


def getTime(num):
    from timeit import timeit
    return timeit(f"fact({num})", "from __main__ import fact", number=1)


#  Pay attention that we are executing the code once at all.
#  The standard value for 'number' is 1000000 (a million times).


# Measuring the time to calculate the factorial of the first multiples of ten.
# Each input is increased by multiplying by ten.

#                                    Input
print(f"fact(10)={fact(10)}")  # Ten
print(f"fact(100)={fact(100)}")  # (previous * 10)
print(f"fact(1000)={fact(1000)}")  # (previous * 10)
print(f"fact(10000)={fact(10000)}")  # (previous * 10)
print(f"fact(100000)={fact(100000)}")  # (previous * 10)
print(f"fact(1000000)={fact(1000000)}")  # (previous * 10)

#                                                                               Seconds
print(f"For fact(10) would spend ---------- {getTime(10)}")  # 9.599999999998499e-06
print(f"For fact(100) would spend --------- {getTime(100)}")  # 1.2100000000000999e-05 (previous * 1.26)
print(f"For fact(1000) would spend -------- {getTime(1000)}")  # 0.00043309999999999876 (previous * 35.8)
print(f"For fact(10000) would spend ------- {getTime(10000)}")  # 0.0228174              (previous * 52.7)
print(f"For fact(100000) would spend ------ {getTime(100000)}")  # 3.1473281999999996     (previous * 137.93)
print(f"For fact(1000000) would spend ----- {getTime(1000000)}")  # 522.3867521999999      (previous * 165.98)
