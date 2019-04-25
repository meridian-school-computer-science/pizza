# classes for pizza with decorator design

class Pizza:
    """
    Base class for the building of a pizza.
        Use decorators to complete the design of each pizza object.


    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Pizza({self.name})"

    def __str__(self):
        return f"{self.name }"
