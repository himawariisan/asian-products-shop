from django.urls import path
from . import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('shop-details/<int:pk>/', views.shop_details, name='shop_details'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('shop-grid/<slug:category_slug>/', views.shop_grid, name='shop_grid_category'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
    path('order-success/', views.order_success, name='order_success'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('shop/category/<slug:category_slug>/', views.shop_grid, name='shop_by_category'),
]
