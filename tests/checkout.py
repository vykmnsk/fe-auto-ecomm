import pytest
from page_objects import products, shop_cart, checkout


@pytest.fixture(scope="function")
def setup_cart(sb):
    products.nav_to_a_product(sb)
    products.pick_product(sb)


def test_checkout_process(sb, setup_cart):
    shop_cart.assert_displayed(sb)
    shop_cart.reject_protection(sb)
    shop_cart.proceed_to_checkout(sb)

    checkout.assert_at_email(sb)
    sb.update_text(checkout.input_email, 'test@example.com')
    checkout.proceed(sb)

    checkout.assert_at_shipping(sb)
    sb.update_text(checkout.input_name, 'The Tester')
    sb.update_text(checkout.input_address, '1 Great Street')
    sb.update_text(checkout.input_city, 'Melbourne')
    sb.select_option_by_text(checkout.input_state, 'VIC')
    sb.update_text(checkout.input_postal, '3000')
    sb.update_text(checkout.input_phone, '0412345678')
    checkout.proceed(sb)

    checkout.assert_at_billing(sb)
