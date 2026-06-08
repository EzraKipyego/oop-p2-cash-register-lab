#!/usr/bin/env python3

class CashRegister:
    """
    Represents a simple cash register that can track purchases, apply discounts, and void transactions.
    """

    def __init__(self, discount=0):
        """
        Initialize the cash register with an optional discount percentage.
        """
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the register.

        item: item name
        price: price per item
        quantity: number of items purchased
        """
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Apply the register discount to the current total.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)

        if float(self.total).is_integer():
            display_total = int(self.total)
        else:
            display_total = self.total

        print(
            f"After the discount, the total comes to ${display_total}."
        )

    def void_last_transaction(self):
        """
        Remove the most recent transaction from the register.
        """
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"] *
            last_transaction["quantity"]
        )

        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])