from django.urls import path
from . import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('shop-details/<int:pk>/', views.shop_details, name='shop_details'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('shop-grid/<slug:category_slug>/', views.shop_grid, name='shop_grid_category'),
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
