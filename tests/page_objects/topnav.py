search_box = 'input[data-qa="input-search-field"]'
search_button = 'input[data-qa="button-text-search"]'
shop_cart_top = 'a.top-nav-show-cart'
ad_modal = '[name="modalclose"]'


def search(sb, criteria):
    sb.update_text(search_box, criteria)
    sb.click(search_button)
    sb.click_if_visible(ad_modal)


def cart_items_count(sb):
    cart_text = sb.get_text(shop_cart_top)
    return int(cart_text)
