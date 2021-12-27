class ControlOfBonuses:
    __slots__ = ["_total"]

    def __init__(self):
        self._total = 0

    def register(self, recordable):
        # hasattr(obj, str_attribute) is the pythonic way to check an object signs a certain protocol.
        # or interface according to its attributes.
        # Better usage than isinstance(obj, class).
        if not hasattr(recordable, "get_bonus"):
            raise AttributeError(f"given object from class {recordable.__class__.__name__} does not have "
                                 f"any get_bonus attribute")
        self._total += recordable.get_bonus()

    @property
    def total(self):
        return self._total
