from models import OrderRepository
from views import OrderView
from controllers import OrderController
from strategies import LoyalCustomerDiscount

def main():
    # 1. Створюємо компоненти MVC
    model = OrderRepository()
    view = OrderView()
    controller = OrderController(model, view)

    # 2. Можна змінити стратегію (Завдання 2)
    # Наприклад, зробимо всі замовлення зі знижкою постійного клієнта
    controller.strategy = LoyalCustomerDiscount()

    # 3. Запуск
    controller.run()

if __name__ == "__main__":
    main()