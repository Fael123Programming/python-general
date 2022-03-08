from account import Account


def method1():
    print("Beginning of method1")
    method2()
    print("End of method1")


def method2():
    print("Beginning of method2")
    account = Account("Rafael Fonseca", 12345)
    try:
        for i in range(1, 15):
            account.deposit(i + 1000)
            print("Balance: $", account.balance)
            if i == 5:
                account = None
    except AttributeError as ae:
        print("Attribute error has been raised:", ae)


if __name__ == "__main__":
    print("Beginning of main")
    method1()
    print("End of main")
    # A partir do momento que uma exceção foi pega e tratada, o fluxo
    # de execução volta ao normal novamente a partir da próxima linha de
    # código depois da sentença try.
