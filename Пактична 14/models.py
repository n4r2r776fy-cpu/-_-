class Order:
    """Клас даних замовлення"""
    def __init__(self, order_id, amount):
        self.id = order_id
        self.amount = amount

class OrderRepository:
    """Клас для зберігання даних у пам'яті"""
    def __init__(self):
        self._orders = []

    def add(self, order):
        self._orders.append(order)

    def get_all(self):
        return self._orders

    def get_total_amount(self):
        return sum(order.amount for order in self._orders)