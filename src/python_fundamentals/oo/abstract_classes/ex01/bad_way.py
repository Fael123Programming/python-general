# Abstract methods are methods which do not provide any implementation in a class
# but let it to children of the class. They work as methods of an interface.

class Pizza:
    def get_radius(self):
        raise NotImplementedError()
    # If a class inherits from Pizza it should implement this method
    # or when an object of that class calls it, an error is raised.
