

class IngredientCostList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._list = []


class Ingredient:

    def __init__(self, name, quantity, date, use_by, refrigerate):
        self.name = name
        self.quantity = quantity
        self.stock_date = date
        self.use_by = use_by
        self.refrigerate = refrigerate



