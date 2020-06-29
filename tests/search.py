import pytest
from page_objects import products


search_box_css = 'input[data-qa="input-search-field"]'
search_button_css = 'input[data-qa="button-text-search"]'
ad_modal_css = '[name="modalclose"]'


def test_search_existing_products(sb):
    criteria = 'office chair mesh'
    sb.assert_element(search_box_css)
    search(sb, criteria)
    products_found = products.get_all_products(sb)
    assert len(products_found) > 0


def search(sb, criteria):
    sb.update_text(search_box_css, criteria)
    sb.click(search_button_css)
    sb.click_if_visible('[name="modalclose"]')
    sb.assert_text('Search Results for')
    sb.assert_text(criteria, 'h1')
