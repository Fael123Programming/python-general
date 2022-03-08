# Exceções Runtime são aquelas causadas em tempo de execução de um script python.
# As mais famosas são:
# NameError, TypeError, KeyError, AttributeError, IndexError, ZeroDivisionError, ValueError
# Todas as excecoes sao filhas da classe Exception, que por sua vez eh filha da classe
# BaseException


def cause_name_error():
    print(variable)  # Variavel nao existe


def cause_type_error():
    values = [8, 1, 4, 2]
    print(values["a"])  # Uso indevido de um tipo de dado


def cause_key_error():
    enchantments = {"powerful": "alakazim-alakazam", "weak": "blabla-blabla"}
    print(enchantments["intermediate"])  # Dicionario nao possui a chave especificada


def cause_attribute_error():
    name = "Python"
    print(name.size)  # Objeto nao possui o atributo especificado


def cause_index_error():
    food = ("pizza", "sandwich", "french fries")
    print(food[3])


def cause_zero_division_error():
    print(1 / 0)


def cause_value_error():
    number = int("asdasd")
    print(number)


if __name__ == "__main__":
    cause_value_error()
