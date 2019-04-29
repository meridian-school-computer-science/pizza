from src.classes_pizza import PizzaType, PizzaElement
from src.pizza_factory import PizzaFactory

print('\nTesting decorator pattern')
cheese = PizzaType('Cheese', 7.99)

print(cheese)

extra_cheese = PizzaElement('Extra Cheese', .30, cheese)
gluten_free = PizzaElement('Gluten Free', 3.99, extra_cheese)
print(extra_cheese, extra_cheese.show_cost)
print(gluten_free, gluten_free.show_cost)


# Now try with a beginning factory
print('\nWith factory pattern')
kitchen = PizzaFactory()
order = {'base': 'cheese',
         'add': 'extra cheese',
         'crust': ''}

my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)


order = {'base': 'sausage',
         'add': '',
         'crust': 'gf'}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)

order = {'base': 'vegetarian',
         'add': 'extra cheese',
         'crust': ''}
my_pizza = kitchen.build_a_pizza(order)
print(my_pizza, my_pizza.show_cost)
