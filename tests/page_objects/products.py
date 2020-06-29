prod_list_url = 'lighting/lamps/desk-lamps'
prod_links_css = "#sbprodgrid a.productbox"
prod_title_css = '[data-qa="text-pdp-product-title"]'
prod_option_css = 'a.js-visual-option'
add_to_cart_button_css = 'input[data-data-qa="button-add-to-cart"]'


def get_all_products(sb):
    return sb.find_elements(prod_links_css)


def pick_product(sb):
    sb.click_if_visible(prod_option_css)
    sb.click(add_to_cart_button_css)


def nav_to_a_product(sb):
    home_url = sb.get_current_url()
    sb.open(home_url + prod_list_url)
    sb.click(prod_links_css)
    sb.assert_element(prod_title_css)
