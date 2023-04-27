def cost_delivery(quantity, *items, discount=0):
    # Розрахунок вартості доставки з урахуванням знижки

    # Розрахунок вартості доставки
    first_item_cost = 5
    next_items_cost = 2
    delivery_cost = first_item_cost + (quantity - 1) * next_items_cost

    # Застосування знижки
    discounted_delivery_cost = delivery_cost * (1 - discount)

    return discounted_delivery_cost
