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
            'combination': 'Combination'
        }
        self._list = []

    def build_a_pizza(self, description):
        base_name = description['base']
        the_base_pizza = PizzaType(self.names[base_name], self.costs[base_name])

        # need to add a size builder
        decorated_pizza = PizzaElement

        # this part needs work with a loop for other adds
        if description['add'] == 'extra cheese':
            decorated_pizza = PizzaElement('Extra Cheese', self.costs['extra'], the_base_pizza)

        # need to implement all crusts
        if description['crust'] == 'gf':
            decorated_pizza = PizzaElement('Gluten Free', self.costs['gf'], the_base_pizza)

        return decorated_pizza



