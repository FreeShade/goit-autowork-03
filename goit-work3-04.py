def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - discount * price

    apply_discount()
    return price
