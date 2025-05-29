import copy


class OrderPrototype:
    def __init__(self):
        self.order_number = None
        self.products = []
        self.total_price = 0.0

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Order {self.order_number}: "
                f"Products: {self.products}, "
                f"Total: ${self.total_price:.2f}")


class Order:
    def __init__(self, prototype=None):
        if prototype is None:
            self.order_number = None
            self.products = []
            self.total_price = 0.0
        else:
            self.order_number = prototype.order_number
            self.products = prototype.products.copy()
            self.total_price = prototype.total_price

    def clone(self):
        """Альтернативный метод клонирования"""
        new_order = Order()
        new_order.order_number = self.order_number
        new_order.products = self.products.copy()
        new_order.total_price = self.total_price
        return new_order


if __name__ == "__main__":
    prototype_order = OrderPrototype()
    prototype_order.order_number = 1001
    prototype_order.products = ["Product A", "Product B", "Product C"]
    prototype_order.total_price = 150.00

    order1 = Order(prototype_order.clone())
    order1.order_number = 1002
    order1.total_price = 200.00

    order2 = prototype_order.clone()
    order2.order_number = 1003
    order2.products.append("Product D")

    order3 = prototype_order.clone()
    order3.order_number = 1004
    order3.products.remove("Product B")
    order3.total_price = 120.00

    print("Prototype Order:")
    print(prototype_order)

    print("\nOrder 1:")
    print(f"Order Number: {order1.order_number}")
    print(f"Products: {order1.products}")
    print(f"Total Price: ${order1.total_price:.2f}")

    print("\nOrder 2:")
    print(f"Order Number: {order2.order_number}")
    print(f"Products: {order2.products}")
    print(f"Total Price: ${order2.total_price:.2f}")

    print("\nOrder 3:")
    print(f"Order Number: {order3.order_number}")
    print(f"Products: {order3.products}")
    print(f"Total Price: ${order3.total_price:.2f}")