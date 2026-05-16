class OrderView:
    def show_menu(self):
        print("\n=== СИСТЕМА КЕРУВАННЯ ЗАМОВЛЕННЯМИ ===")
        print("1. Додати замовлення")
        print("2. Переглянути список замовлень")
        print("3. Загальна сума")
        print("0. Вихід")
        return input("Виберіть дію: ")

    def get_order_input(self):
        try:
            order_id = int(input("Введіть ID: "))
            amount = float(input("Введіть суму: "))
            return order_id, amount
        except ValueError:
            print("Помилка! Вводьте тільки числа.")
            return None

    def show_orders(self, orders):
        print("\n--- Список замовлень ---")
        if not orders:
            print("Список порожній.")
        for o in orders:
            print(f"ID: {o.id} | Сума: {o.amount:.2f}")

    def show_total(self, total):
        print(f"\nЗагальна сума всіх замовлень: {total:.2f}")

    def show_message(self, message):
        print(f">> {message}")