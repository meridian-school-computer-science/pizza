from src.pizza_factory import PizzaFactory


# Now try with a beginning factory
print('\nWith factory pattern')
kitchen = PizzaFactory()
order = {'base': 'cheese',
         'add': ['extra cheese'],
         'remove': [''],
         'size': 'small',
         'crust': 'regular'}

my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)


order = {'base': 'sausage',
         'add': [''],
         'remove': [''],
         'size': 'medium',
         'crust': 'thin'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'sausage',
         'add': [''],
         'remove': [''],
         'size': 'large',
         'crust': 'thin'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'sausage',
         'add': ['extra cheese'],
         'remove': [''],
         'size': 'large',
         'crust': 'gluten-free'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'vegetarian',
         'add': ['extra cheese', 'olives'],
         'remove': ['olives'],
         'size': 'slice',
         'crust': 'cheese filled'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)
