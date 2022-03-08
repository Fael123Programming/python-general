from address import Address
from datetime import date


class AccountOwner:
    __slots__ = ["_name", "_address", "_profession", "_date_of_birth"]

    def __init__(self, name: str, address: Address, profession: str, date_of_birth: date):
        self._name = name
        self._address = address
        self._profession = profession
        self._date_of_birth = date_of_birth

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession: str):
        self._profession = profession

    @property
    def date_of_birth(self):
        return self._date_of_birth

    def __str__(self):
        return f"{{name={self._name}, address={self._address}, profession={self._profession}, " \
               f"date_of_birth={self._date_of_birth.__str__()}}}"

    # def __repr__(self):
    #     return f"Owner(\"{self._name}\", \"{self._address}\")"
