from existing_class import ExistingClass
from service import Service

class Adapter(ExistingClass, Service):
    def __init__(self):
        pass

    def method(self, data):
        # Do something on data to put it understandable to the service method.
        # data = result of some process...
        return self.service_method(data)