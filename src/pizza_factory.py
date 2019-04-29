from src.classes_pizza import Pizza, PizzaType, PizzaElement


class PizzaFactory(Pizza):

    def __init__(self):
        self.costs = {'cheese': 7.99,
                      'pepperoni': 8.99,
                      'sausage': 8.99,
                      'vegetarian': 8.99,
                      'combination': 9.99,
                      'extra': .3,
                      'remove': -.25,
                      'gf': 3.99}
        self.base = PizzaType
        self.decorated = PizzaElement
        self.add_on = PizzaElement
        self._list = []

    def build_a_pizza(self, description):
        if description['base'] == 'cheese':
            self.base = PizzaType('Cheese', self.costs['cheese'])
        elif description['base'] == 'pepperoni':
            self.base = PizzaType('Pepperoni', self.costs['peperoni'])
        elif description['base'] == 'sausage':
            self.base = PizzaType('Sausage', self.costs['sausage'])
        elif description['base'] == 'vegetarian':
            self.base = PizzaType('Vegetarian', self.costs['vegetarian'])
        elif description['base'] == 'combination':
            self.base = PizzaType('Combination', self.costs['combination'])

        # need to add a size builder


        # this part needs work with a loop for other adds
        if description['add'] == 'extra cheese':
            self.decorated = PizzaElement('Extra Cheese', self.costs['extra'], self.base)

        # need to implement all crusts
        if description['crust'] == 'gf':
            self.decorated = PizzaElement('Gluten Free', self.costs['gf'], self.base)

        return self.decorated



