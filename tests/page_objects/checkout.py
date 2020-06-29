header_email = 'Where shall we email your receipt?'
header_shipping = 'Enter Shipping Address'
header_billing = 'Select Payment Method'

input_email = 'input[type="email"]'
input_name = 'input#full_name'
input_address = 'input#address_1'
input_city = 'input#city'
input_state = 'select#state_id'
input_postal = 'input#postal_code'
input_phone = 'input#phone'
btn_continue = 'input[value="Continue"]'


def assert_at_email(sb):
    sb.assert_text(header_email)


def assert_at_shipping(sb):
    sb.assert_text(header_shipping)


def assert_at_billing(sb):
    sb.assert_text(header_billing)


def proceed(sb):
    sb.click(btn_continue)
