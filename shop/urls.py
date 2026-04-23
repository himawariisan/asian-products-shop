from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [    
    path('', views.index, name='index'),
    path('shop-details/<int:pk>/', views.shop_details, name='shop_details'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
