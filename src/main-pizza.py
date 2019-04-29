from src.pizza_factory import PizzaFactory


# Now try with a beginning factory
print('\nWith factory pattern')
kitchen = PizzaFactory()
order = {'base': 'cheese',
         'add': 'extra cheese',
         'size': 'small',
         'crust': 'regular'}

my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)


order = {'base': 'sausage',
         'add': '',
         'size': 'medium',
         'crust': 'thin'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'sausage',
         'add': '',
         'size': 'large',
         'crust': 'thin'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'sausage',
         'add': '',
         'size': 'large',
         'crust': 'gluten-free'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'vegetarian',
         'add': 'extra cheese',
         'size': 'slice',
         'crust': 'cheese filled'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)
