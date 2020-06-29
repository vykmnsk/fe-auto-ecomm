cart_page_header = "Shopping Cart"


def assert_displayed(sb):
    sb.assert_text(cart_page_header)


def reject_protection(sb):
    sb.click('label[for="freight_protection_no"]')
    sb.assert_text('No thanks', 'label[for="freight_protection_no"]')
    sb.wait_for_text_not_visible('Updating', '#txtTotalDisplay')


def proceed_to_checkout(sb):
    checkout_button = sb.find_visible_elements('input#btnCheckout')[0]
    checkout_button.click()
