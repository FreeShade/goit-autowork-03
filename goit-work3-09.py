def cost_delivery(quantity, *_, discount=0):
    """Знаходить суму трьох параметрів.

    Перший параметр обов'язковий, два інших за замовчанням дорівнюють 2 і 3"""

    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
