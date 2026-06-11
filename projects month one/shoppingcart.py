def Additem(cart,item):
    cart.append(item)

def Removeitem(cart,item):

    if item in cart:
        cart.remove(item)
    else:
        print("item is not in the cart and is not possible to remove")

def show(cart):
    print(cart)

def main():
    cart=[]
    Additem(cart,input("enter an item to add to cart: "))
    Additem(cart,input("enter another item to add to cart: ")   )
    show(cart)
    Removeitem(cart,input("enter an item to remove from cart: "))
    show(cart)

main()