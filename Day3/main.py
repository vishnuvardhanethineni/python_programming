import ecommerce_utils
cart={}
def add_cart(item,price):
    if item in cart:
        cart[item]+=price
    cart[item]=price
def remove_cart(item):
    del cart[item]
add_cart('laptop',50000)
add_cart('mouse',500)
add_cart('keyboard',1500)
ecommerce_utils.generate_invoice(cart,10,18)