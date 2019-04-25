# classes for pizza with decorator design


class Pizza:
    """
    Base class for the building of a pizza.
        Use decorators to complete the design of each pizza object.


    """

    def __init__(self, name, cost):
        self.name = name
        self.cost = float(cost)

    def __repr__(self):
        return f"Pizza({self.name})"

    def __str__(self):
        return f"{self.name} - ${self.cost:.2f}"

    def get_cost(self):
        return self.cost


class PizzaElement(Pizza):

    def __init__(self, name, cost):
        super().__init__(name, cost)

    def get_cost(self):



