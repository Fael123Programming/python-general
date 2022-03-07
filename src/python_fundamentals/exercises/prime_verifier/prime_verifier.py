class PrimeVerifier:

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 0:
            number *= -1
        if number == 2 or number == 3 or number == 5 or number == 7:
            return True
        divisors = 1
        sqrt = int(number ** 0.5)
        for i in range(2, sqrt + 1):
            if number % i == 0:
                divisors += 1
        return divisors == 1


if __name__ == "__main__":
    pv = PrimeVerifier()
    print(pv.is_prime(67280421310721))
