from .models import Cart

def cart_context(request):
    cart = None
    cart_item_count = 0
    cart_total = 0

    if request.session.session_key:
        try:
            cart = Cart.objects.get(session_key=request.session.session_key)
            cart_item_count = cart.items.count()
            cart_total = cart.get_total()
        except Cart.DoesNotExist:
            pass

    return {
        'cart_item_count': cart_item_count,
        'cart_total': cart_total,
    }  