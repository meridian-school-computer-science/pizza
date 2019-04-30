from src.classes_pizza import Pizza, PizzaType, PizzaElement


class PizzaFactory(Pizza):

    def __init__(self):
        self.costs = {
            'cheese': 7.99,
            'pepperoni': 8.99,
            'sausage': 8.99,
            'vegetarian': 8.99,
            'combination': 9.99,
            'extra': .3,
            'remove': -.25,
            'gf': 3.99
        }
        self.names = {
            'cheese': 'Cheese',
            'pepperoni': 'Pepperoni',
            'sausage': 'Sausage',
            'vegetarian': 'Vegetarian',
            'combination': 'Combination',
            'special': 'Special'
        }
        self.sizes = {
            'slice': 'Slice',
            'individual': 'Individual',
            'small': 'Small',
            'medium': 'Medium',
            'large': 'Large'
        }
        self.size_costs = {
            'slice': -4.99,
            'individual': -2.99,
            'small': -1.99,
            'medium': 0,
            'large': 1.99
        }
        self.add = {
            'extra cheese': 'Extra Cheese',
            'extra veggies': 'Extra Veggies',
            'onions': 'Onions',
            'olives': 'Olives',
            'extra sauce': 'Extra Sauce',
            'double meat': 'Double Meat',
            'banana peppers': 'Banana Peppers'
        }
        self.add_costs ={
            'extra cheese': .5,
            'extra veggies': .4,
            'onions': .25,
            'olives': .25,
            'extra sauce': .3,
            'double meat': .5,
            'banana peppers': .25
        }
        self.remove = {
            'cheese': 'hold Cheese',
            'onions': 'hold Onions',
            'olives': 'hold Olives',
            'sauce': 'hold Sauce',
            'peppers': 'hold Peppers'
        }
        self.remove_save = {
            'cheese': .25,
            'onions': .25,
            'olives': .25,
            'sauce': .25,
            'peppers': .25
        }
        self.crusts = {
            'thin': 'Thin Crust',
            'regular': 'Regular Crust',
            'gluten-free': 'Gluten-Free',
            'thick': 'Thick Crust',
            'cheese filled': 'Cheese Filled Crust'
        }
        self.crusts_costs = {
            'thin': 0,
            'regular': 0,
            'gluten-free': 4.99,
            'thick': 1.00,
            'cheese filled': 1.50
        }
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



