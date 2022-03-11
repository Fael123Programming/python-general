from collections import UserDict

"""
    The following class implements a dict type where
    all keys are converted to their respective string
    representation.
"""


class StrDict(UserDict):
    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == "__main__":
    strDict = StrDict()
    strDict[120] = "one hundred twenty"
    strDict[[1, 2, 3]] = "A list of numbers"
    print(strDict)
    print(strDict["[1, 2, 3]"])

