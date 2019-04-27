from src.classes_pizza import PizzaType, PizzaElement

cheese = PizzaType('Cheese', 7)

print(cheese)

extra_cheese = PizzaElement('Extra Cheese', .40, cheese)
gluten_free = PizzaElement('Gluten Free', .25, extra_cheese)
print(extra_cheese, extra_cheese.show_cost)
print(gluten_free, gluten_free.show_cost)
