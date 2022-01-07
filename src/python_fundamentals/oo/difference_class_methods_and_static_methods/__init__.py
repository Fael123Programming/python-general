class ADataModel:

    @staticmethod
    def static_method():
        """
            Static methods are class close-related actions but not something
            that must be done uniquely per instance. They do not receive a
            mandatory first argument (like self or cls). Indeed, they are
            outside functions that have a close relationship with your class.
            That is why it makes sense to put it inside your class.
         """

    @classmethod
    def class_method(cls):
        """
            This should also do something that has a relationship with
            your class, but usually, actions that involve manipulating
            different structures of data to instantiate objects of the
            corresponding class like create runtime objects from a csv
            (comma separated values) file, a json file etc. They receive
            a first mandatory argument which refers to a class object.
            Both can be called either through an instance or the class
            itself, but it is recommended to use them only through class
            reference.
        """