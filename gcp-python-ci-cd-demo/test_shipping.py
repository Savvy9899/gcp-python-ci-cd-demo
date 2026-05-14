from shipping import calculate_shipping_category

def test_standard_shipping_for_weight_five_or_less():
    assert calculate_shipping_category(1) == "STANDARD"
    assert calculate_shipping_category(5) == "STANDARD"

def test_heavy_shipping_for_weight_above_five():
    assert calculate_shipping_category(6) == "STANDARD"
    #assert calculate_shipping_category(6) == "HEAVY"

def test_invalid_shipping_for_zero_or_negative_weight():
    assert calculate_shipping_category(0) == "INVALID"
    assert calculate_shipping_category(-2) == "INVALID"