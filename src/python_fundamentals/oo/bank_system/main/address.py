class Address:
    __slots__ = ["_country", "_state", "_city", "_neighbourhood", "_street", "_number", "_extra"]

    def __init__(self, country: str, state: str, city: str, neighbourhood: str, street: str, number: int, extra=""):
        self._country = country
        self._state = state
        self._city = city
        self._neighbourhood = neighbourhood
        self._street = street
        self._number = number
        self._extra = extra

    @property
    def country(self):
        return self._country

    @property
    def state(self):
        return self._state

    @property
    def city(self):
        return self._city

    @property
    def neighbourhood(self):
        return self._neighbourhood

    @property
    def street(self):
        return self._street

    @property
    def number(self):
        return self._number

    @property
    def extra(self):
        return self._extra

    def __str__(self):
        return f"{{country={self._country}, state={self._state}, city={self._city}, neighbourhood={self._neighbourhood}," \
               f"street={self._street}, number={self._number}, extra={self._extra}}}"

