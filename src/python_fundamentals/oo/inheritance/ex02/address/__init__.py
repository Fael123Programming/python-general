class Address:
    __slots__ = ["_country", "_state", "_city", "_neighbourhood", "_street", "_number"]

    def __init__(self, country: str, state: str, city: str, neighbourhood: str, street: str, number: int):
        self._country = country
        self._state = state
        self._city = city
        self._neighbourhood = neighbourhood
        self._street = street
        self._number = number

    def __init__(self):
        pass

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def neighbourhood(self):
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, neighbourhood: str):
        self._neighbourhood = neighbourhood

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number
