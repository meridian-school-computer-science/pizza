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
        return f"{self.name}"

    def get_cost(self):
        return self.cost


class PizzaType(Pizza):

    def __init__(self, name, cost):
        super().__init__(name, cost)


class PizzaElement(Pizza):

    def __init__(self, name, cost, pizza):
        super().__init__(name, cost)
        self.decorate = pizza

    def get_cost(self):
        return self.cost + self.decorate.get_cost()

    def __str__(self):
        return self.decorate.__str__() + f" + {self.name}"

    @property
    def show_cost(self):
        return f" ${self.get_cost():.2f}"

