from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def checkout_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            cart_items.delete()
            return redirect('order_success')
    else:
        form = OrderForm()

    context = {
        'user': user,
        'cart_items': cart_items,
        'form': form
    }
    return render(request, 'order/checkout.html', context)


def order_success(request):
    return render(request, 'order/order_success.html')