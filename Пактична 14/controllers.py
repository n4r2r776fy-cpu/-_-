from models import Order
from strategies import RegularPrice

class OrderController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # За замовчуванням використовуємо звичайну стратегію
        self.strategy = RegularPrice()

    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == "1":
                data = self.view.get_order_input()
                if data:
                    order_id, amount = data
                    # Застосовуємо стратегію розрахунку ціни перед збереженням
                    final_amount = self.strategy.calculate(amount)
                    new_order = Order(order_id, final_amount)
                    self.model.add(new_order)
                    self.view.show_message(f"Додано! (Фінальна ціна: {final_amount})")
            
            elif choice == "2":
                self.view.show_orders(self.model.get_all())
            
            elif choice == "3":
                self.view.show_total(self.model.get_total_amount())
            
            elif choice == "0":
                self.view.show_message("Програма завершена.")
                break
            else:
                self.view.show_message("Невірний вибір!")