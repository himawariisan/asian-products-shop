from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def blog_details(request):
    return render(request, 'shop/blog-details.html')

def blog(request):
    return render(request, 'shop/blog.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def shopping_cart(request):
    return render(request, 'shop/shopping-cart.html')

def shop_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/shop-details.html', {'product': product})

def shop_grid(request):
    products = Product.objects.all()
    return render(request, 'shop/shop-grid.html', {'products': products})

def get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)

    return cart

def cart_detail(request): 
    cart = get_or_create_cart(request)
    items = cart.items.all()

    return render(request, 'shop/shopping-cart.html', {
        'cart': cart,
        'items': items,
    })

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_or_create_cart(request)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

