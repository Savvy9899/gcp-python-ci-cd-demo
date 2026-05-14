def calculate_shipping_category(weight):
    if weight <= 0:
        return "INVALID"

    if weight <= 5:
        return "STANDARD"

    return "HEAVY"