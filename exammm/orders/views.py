from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Order
from products.models import Product
from products.views import get_user_role


@login_required
def order_list(request):
    user_role = get_user_role(request.user)

    if user_role in ['admin', 'manager']:
        orders = Order.objects.select_related('product', 'user')
    else:
        orders = Order.objects.filter(user=request.user).select_related('product', 'user')

    return render(request, 'orders/order_list.html', {
        'orders': orders,
        'user_role': user_role
    })


@login_required
def order_create(request):
    user_role = get_user_role(request.user)
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, pk=product_id)

        total_price = product.final_price * quantity

        Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            price=total_price
        )
        messages.success(request, 'Заказ успешно создан.')
        return redirect('orders:order_list')

    return render(request, 'orders/order_form.html', {
        'products': products,
        'user_role': user_role
    })


@login_required
def order_update(request, pk):
    user_role = get_user_role(request.user)
    order = get_object_or_404(Order, pk=pk)

    if user_role == 'client' and order.user != request.user:
        messages.error(request, 'Нет доступа.')
        return redirect('orders:order_list')

    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, pk=product_id)

        order.product = product
        order.quantity = quantity
        order.price = product.final_price * quantity
        order.save()

        messages.success(request, 'Заказ обновлён.')
        return redirect('orders:order_list')

    return render(request, 'orders/order_form.html', {
        'order': order,
        'products': products,
        'user_role': user_role
    })


@login_required
def order_delete(request, pk):
    user_role = get_user_role(request.user)
    order = get_object_or_404(Order, pk=pk)

    if user_role == 'client' and order.user != request.user:
        messages.error(request, 'Нет доступа.')
        return redirect('orders:order_list')

    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Заказ удалён.')
        return redirect('orders:order_list')

    return render(request, 'orders/order_confirm_delete.html', {
        'order': order,
        'user_role': user_role
    })