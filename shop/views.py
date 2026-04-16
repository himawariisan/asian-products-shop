from django.shortcuts import render

def index(request):
    return render(request, 'shop/index.html')

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

def shop_details(request):
    return render(request, 'shop/shop-details.html')
