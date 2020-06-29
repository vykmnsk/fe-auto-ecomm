import pytest
from page_objects import topnav, products, shop_cart


def test_add_product(sb):
    products.nav_to_a_product(sb)
    count_before = topnav.cart_items_count(sb)
    products.pick_product(sb)
    shop_cart.assert_displayed(sb)
    count_after = topnav.cart_items_count(sb)
    assert count_after == count_before + 1
