from .models import CartItem

def cart_item_count(request):
    count = 0
    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).count()
    else:
        cart = request.session.get('cart', {})
        count = sum(cart.values())
    return {'cart_item_count': count}