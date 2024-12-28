
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, reverse

from store.models import Product, Carts, Order


# Create your views here.

def index (request):
    products = Product.objects.all()

    return render(request, 'store/index.html', context={"products" : products})

def product_detail (request, slug) :
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product" : product})

def add_to_cart (request, slug) :
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Carts.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)
    if created :
        cart.order.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug":slug}))
