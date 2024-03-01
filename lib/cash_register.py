class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount

    def add_item(self, item, price, quantity=1):
        self.items.append((item, price, quantity))
        self.total += price * quantity
        return f"Added {quantity} {item}(s) to the cart. Total: ${self.total}"

    def apply_discount(self):
        if self.discount:
            self.total -= self.discount
            return f"After the discount, the total comes to ${self.total}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item, last_price, last_quantity = self.items.pop()
            self.total -= last_price * last_quantity
            return f"Voided the last transaction. Total: ${self.total}"
        else:
            return "There are no transactions to void."

    def get_item_price(self, item):
        for i in range(len(self.items) - 1, -1, -1):
            current_item, price, quantity = self.items[i]
            if current_item == item:
                return price
        return None

    def get_item_total(self, item):
        return sum(price * quantity for price, quantity, name in self.items if name == item)

    def get_item_quantity(self, item):
        return sum(quantity for price, quantity, name in self.items if name == item)

    def reset_register_totals(self):
        self.total = 0.0
        self.items = []

    def get_all_items(self):
        return [item for item, price, quantity in self.items]

    def get_all_items_including_multiples(self):
        return [(item, quantity) for item, price, quantity in self.items]
