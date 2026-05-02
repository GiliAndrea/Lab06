from dataclasses import dataclass
from datetime import datetime

@dataclass
class Sale:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float
    ricavo: float

    def ricavoSale(self):
        self.ricavo = self.Quantity * self.Unit_sale_price

    def __eq__(self, other):
        return (self.Retailer_code == other.Retailer_code and self.Product_number == other.Product_number
                   and self.Order_method_code == other.Order_method_code)

    def __hash__(self):
        return hash(self.Retailer_code + self.Product_number + self.Order_method_code)

    def __str__(self):
        return (f"Data: {self.Date}, Ricavo: {self.ricavoSale()}, "
                f"Retailer: {self.Retailer_code}, Product: {self.Product_number}")
