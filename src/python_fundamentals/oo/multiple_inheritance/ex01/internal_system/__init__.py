class InternalSystem:

    @staticmethod
    def login(authenticable):
        authenticable.authenticate()  # If authenticable has no attribute authenticate, an error will be raised.
        # if username and password are correct:
        #     return True
        # return False

