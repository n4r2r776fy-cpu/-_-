from abc import ABC, abstractmethod

class IPriceStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class RegularPrice(IPriceStrategy):
    def calculate(self, price):
        return price

class LoyalCustomerDiscount(IPriceStrategy):
    def calculate(self, price):
        return price * 0.9  # 10% знижка

class BulkOrderDiscount(IPriceStrategy):
    def calculate(self, price):
        return price * 0.8 if price > 1000 else price