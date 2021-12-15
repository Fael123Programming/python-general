class Customer:
    """
    The class Customer represents a simple customer data set that contains basic information
    about a customer which would be significant in a prototype of a bank system.
    """

    def __init__(self, name: str, date_of_birth: str, cpf: str):
        self._name = name
        self._date_of_birth = date_of_birth
        self._cpf = cpf

    @property
    def name(self):
        return self._name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def cpf(self):
        return self._cpf

    def __str__(self):
        return f"{{name: {self._name}, date_of_birth: {self._date_of_birth}, cpf: {self._cpf}}}"
