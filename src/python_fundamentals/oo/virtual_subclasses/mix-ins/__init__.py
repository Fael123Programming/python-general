from abc import ABC, abstractmethod

# Mix-ins are small classes that are supposed to be inherited to add functionality to a specific class.
# They usually provide additional methods to a class.
# Here goes an example!


class Account:

    def __init__(self):
        # All other attributes should come here!
        self._balance = 0

    # All the resting code comes here!

    def deposit(self, amount):
        self._balance += amount

    @property
    def balance(self):
        return self._balance


class TaxableMixIn(ABC):
    """
        Adds the ability of providing a method to get a tax value
        of another value a specific object has.
    """
    @abstractmethod
    def get_tax(self):
        pass


class CurrentAccount(Account):

    def __init__(self):
        super().__init__()

    def get_tax(self):
        return self.balance * 0.01  # 1% of balance


class InvestmentAccount(Account):

    def __init__(self):
        super().__init__()

    def get_tax(self):
        return self.balance * 0.03


class LifeInsurance:

    def __init__(self, value, owner):
        self._value = value
        self._owner = owner

    def get_tax(self):
        return self._value * 0.05 + 50


class TaxableHandler:

    @staticmethod
    def calculate_total_tax(list_of_taxable):
        total = 0
        for taxable in list_of_taxable:
            if isinstance(taxable, TaxableMixIn):
                total += taxable.get_tax()
            else:
                raise ValueError("not a taxable object inside list")
        return total


if __name__ == "__main__":
    TaxableMixIn.register(CurrentAccount)  # CurrentAccount signs the contract of the mix-in or interface
    TaxableMixIn.register(LifeInsurance)  # LifeInsurance signs the contract of the mix-in or interface
    TaxableMixIn.register(InvestmentAccount)
    ca1 = CurrentAccount()
    ca1.deposit(1000)
    ca2 = CurrentAccount()
    ca2.deposit(5000)
    li1 = LifeInsurance(10000, "Peter Park")
    li2 = LifeInsurance(2000000, "Cristiano Ronaldo")
    ia1 = InvestmentAccount()
    ia1.deposit(50000)
    ia2 = InvestmentAccount()
    ia2.deposit(80000)
    taxable_objects = [ca1, ca2, li1, li2, ia1, ia2]
    print(f"Total is ${TaxableHandler.calculate_total_tax(taxable_objects)}")
    print(TaxableHandler.calculate_total_tax)
    print(help(TaxableMixIn))
