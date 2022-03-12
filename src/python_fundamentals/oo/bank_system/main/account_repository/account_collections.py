from collections.abc import MutableSequence, MutableMapping

from python_fundamentals.oo.bank_system.main.accounts import Account


"""
    A list-like type which accepts only Account objects to be inserted.
"""


class Accounts(MutableSequence):
    _data = []

    def __len__(self):
        return self._data.__len__()

    def __getitem__(self, pos):
        return self._data[pos]

    def __setitem__(self, key, value):
        if not isinstance(value, Account):
            raise TypeError("Only Account objects are allowed to be inserted")
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def insert(self, key, value):
        if not isinstance(value, Account):
            raise TypeError("Only Account objects are allowed to be inserted")
        return self._data.insert(key, value)


"""
    A dict-like type which accepts for its mapping only
    Account objects (directly or indirectly).
"""


class AccountsMapping(MutableMapping):
    _dict = {}

    def __getitem__(self, k):
        return self._dict[k]

    def __len__(self) -> int:
        return self._dict.__len__()

    def __iter__(self):
        return self._dict.__iter__()

    def __setitem__(self, k, v):
        if not isinstance(v, Account):
            raise TypeError("Only Account objects are allowed to be inserted")
        self._dict[k] = v

    def __delitem__(self, v):
        for key, value in self._dict.items():
            if value == v:
                del self._dict[key]
