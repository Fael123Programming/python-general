from collections.abc import MutableSequence

from python_fundamentals.exercises.readingwithcsv.employee import Employee


class Employees(MutableSequence):
    _data = []  # This is the underlying data structure holding all data.

    # Use isinstance() or issubclass() to check an object's parenthood.
    def __contains__(self, item):
        return self._data.__contains__(item)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, pos):
        return self._data[pos]

    def __setitem__(self, key, value):
        if not isinstance(value, Employee):  # Only employees are allowed here.
            raise TypeError("Only Employee objects are allowed to be inserted")
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def insert(self, key, value):  # Provides the append() method.
        if not isinstance(value, Employee):  # Only employees are allowed here.
            raise TypeError("Only Employee objects are allowed to be inserted")
        return self._data.insert(key, value)

    # Toda coleção deve herdar dessas classes ABCs: Container, Iterable e Sized. Ou implementar
    # seus protocolos: __contains__, __iter__ e __len__.
