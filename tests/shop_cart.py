import pytest
from page_objects import topnav, products

cart_page_header = "Shopping Cart"


def test_add_product(sb):
    products.nav_to_a_product(sb)
    count_before = cart_items_count(sb)
    products.pick_product(sb)
    sb.assert_text(cart_page_header)
    count_after = cart_items_count(sb)
    assert count_after == count_before + 1


def cart_items_count(sb):
    cart_text = sb.get_text(topnav.shop_cart_top_css)
    return int(cart_text)
