class Owner:
    __slots__ = ["_name", "_address"]

    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return f"{{name: {self._name}, address: {self._address}}}"

    def __repr__(self):
        return f"Owner(\"{self._name}\", \"{self._address}\")"
