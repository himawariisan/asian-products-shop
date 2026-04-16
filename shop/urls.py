from django.urls import path
from . import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('shop-details/', views.shop_details, name='shop_details'),
    path('shop-grid/', views.index, name='shop_grid'),
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
