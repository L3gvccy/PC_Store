from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib import messages, auth
=======
>>>>>>> 4efcee2 (Add cart)
=======
from django.contrib import messages, auth
>>>>>>> 078958a (cart update notifications)
from .models import CartItem
from components.models import Product

@login_required
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d39d9a1 (add clear_cart)
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, "Ваш кошик очищено.")
    return redirect('view_cart')

@login_required
<<<<<<< HEAD
=======
>>>>>>> 4efcee2 (Add cart)
=======
>>>>>>> d39d9a1 (add clear_cart)
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')

@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a834df8 (update cart view)
def view_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "Вам потрібно увійти в систему, щоб переглянути кошик.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    total_price = sum(item.product.price * item.quantity for item in cart_items)
=======
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
<<<<<<< HEAD
<<<<<<< HEAD
    total_price = sum(item.cpu.price * item.quantity for item in cart_items)
>>>>>>> 4efcee2 (Add cart)
=======
=======
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
>>>>>>> 31afb41 (update cart, add cpu detail, add cart item cout)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
>>>>>>> f236aa0 (update cart)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request, 'cart/cart.html', context)

<<<<<<< HEAD
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Вам потрібно увійти в систему, щоб додати товар до кошика.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
=======
    return render(request, 'components/cart.html', context)
=======
    return render(request, 'cart/cart.html', context)
>>>>>>> f236aa0 (update cart)

@login_required
def add_to_cart(request, product_id):
>>>>>>> 4efcee2 (Add cart)
=======
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Вам потрібно увійти в систему, щоб додати товар до кошика.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
>>>>>>> 078958a (cart update notifications)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product = product)

    if not created:
<<<<<<< HEAD
        if cart_item.quantity >= product.quantity:
            messages.warning(request, "Неможливо додати більше. Товар закінчується на складі.")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"Товар {product.name} успішно додано до кошика.")

<<<<<<< HEAD
    return redirect(request.META.get('HTTP_REFERER', '/'))

def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if item.quantity < item.product.quantity:
        item.quantity += 1
        item.save()
    else:
        messages.warning(request, "Неможливо додати більше. Товар закінчується на складі.")

=======
        cart_item.quantity += 1
        cart_item.save()

>>>>>>> 4efcee2 (Add cart)
    return redirect('view_cart')  
=======
    return redirect(request.META.get('HTTP_REFERER', '/'))
>>>>>>> 078958a (cart update notifications)
