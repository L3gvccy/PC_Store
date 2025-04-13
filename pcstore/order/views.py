from django.shortcuts import render, redirect
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib import messages
=======
>>>>>>> c4c30a5 (Add order)
=======
from django.contrib import messages
>>>>>>> ea4c7eb (order error exception)
from cart.models import CartItem
from .models import Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def checkout_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
<<<<<<< HEAD
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if cart_items.count() == 0:
        messages.error(request, "Додайте хочаб один товар, щоб створити замволення.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
=======
>>>>>>> c4c30a5 (Add order)

    if cart_items.count() == 0:
        messages.error(request, "Додайте хочаб один товар, щоб створити замволення.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a5d3f0 (Update order and cart view)
            if order.delivery_type != 'post_office':
                order.post_company = '---------'
            order.user = user
            order.first_name = request.POST['first_name']
            order.last_name = request.POST['last_name']
            order.email = request.POST['email']
            order.phone_number = request.POST['phone_number']
<<<<<<< HEAD
            order.total_price = total_price
=======
            order.user = user
>>>>>>> c4c30a5 (Add order)
=======
>>>>>>> 77ce071 (order views update)
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

<<<<<<< HEAD
                item.product.quantity -= item.quantity
                item.product.save()

=======
>>>>>>> c4c30a5 (Add order)
            cart_items.delete()
            return redirect('order_success')
    else:
        form = OrderForm()

    context = {
        'user': user,
        'cart_items': cart_items,
<<<<<<< HEAD
        'form': form,
        'total_price': total_price,
    }

    

=======
        'form': form
    }
>>>>>>> c4c30a5 (Add order)
    return render(request, 'order/checkout.html', context)


def order_success(request):
<<<<<<< HEAD
    return render(request, 'order/order_success.html')

def view_orders(request):
    if not request.user.is_authenticated:
        messages.error(request, "Вам потрібно увійти в систему, щоб переглянути замовлення.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'order/my_orders.html', context)
=======
    return render(request, 'order/order_success.html')
>>>>>>> c4c30a5 (Add order)
