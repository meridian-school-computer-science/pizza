from src.classes_pizza import Pizza, PizzaType, PizzaElement
from src.constants_file import *


class PizzaFactory(Pizza):

    def __init__(self):
        # Don't include call to super init
        self.costs = BASE_PIZZA_COSTS
        self.names = BASE_PIZZA_NAMES
        self.sizes = PIZZA_SIZES
        self.size_costs = PIZZA_SIZES_COST
        self.add = INGREDIENT_ADDS
        self.add_costs = INGREDIENT_ADDS_COSTS
        self.remove = INGREDIENT_REMOVES
        self.remove_save = INGREDIENT_REMOVES_SAVES
        self.crusts = CRUST_NAMES
        self.crusts_costs = CRUST_COSTS

        # not sure if this is needed
        self._list = []

    def build_a_pizza(self, description):
        base_name = description['base']
        size = description['size']
        crust = description['crust']
        adds = description['add']
        removes = description['remove']

        # start the building with a base
        the_base_pizza = PizzaType(self.names[base_name], self.costs[base_name])
        # then add the size
        the_sized_pizza = PizzaElement(self.sizes[size], self.size_costs[size], the_base_pizza)
        # then add the crust choice
        the_finished_pizza = PizzaElement(self.crusts[crust], self.crusts_costs[crust], the_sized_pizza)

        if adds != ['']:
            for each_add in adds:
                the_finished_pizza = PizzaElement(self.add[each_add], self.add_costs[each_add], the_finished_pizza)

        if removes != ['']:
            for each_remove in removes:
                the_finished_pizza = PizzaElement(self.remove[each_remove], self.remove_save[each_remove], the_finished_pizza)


        return the_finished_pizza



