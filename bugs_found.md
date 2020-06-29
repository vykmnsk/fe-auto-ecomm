Bugs found
==========


### 1. Inconsistent HTML attribute

On any Product Details page, for example:
https://www.templeandwebster.com.au/York-Steel-Table-Lamps-ORIB3238.html 

[ADD TO CART] button HTML contains attribute
	
	data-data-qa="button-add-to-cart"

Expected instead:
	
	data-qa="button-add-to-cart"
