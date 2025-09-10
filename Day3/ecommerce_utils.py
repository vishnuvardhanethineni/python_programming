def applydiscount(price, discount):
    return price - (price *0.01*discount)
def add_gst(price,gst=18):
    return price + (price*0.01*gst)
def generate_invoice(cart,discount=0,gst=18):
    print('-----------INVOICE-----------')
    for i in cart:
        print(f"{i} \t\t-\t{cart[i]}")
    print('-----------------------------')
    total=sum(cart.values())
    print(f"Subtotal \t\t:\t {total}")
    total=applydiscount(total,discount)
    print(f"After discount {discount} \t:\t {total}")
    total=add_gst(total,gst)
    print(f'After gst {gst} \t\t:\t {total}')
    print('------------------------------')