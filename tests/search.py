import pytest
from page_objects import products, topnav


@pytest.mark.parametrize('criteria', ['office chair mesh', 'desk lamps steel'])
def test_search_existing_products(sb, criteria):
    topnav.search(sb, criteria)
    products.assert_at_prod_list(sb)
    sb.assert_text(criteria, 'h1')
    products_found = products.get_all_products(sb)
    assert len(products_found) > 0
