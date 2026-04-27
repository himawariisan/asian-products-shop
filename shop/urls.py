from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [    
    path('', views.index, name='index'),
    path('shop-details/<int:pk>/', views.shop_details, name='shop_details'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
]
