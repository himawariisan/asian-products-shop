from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.session_key})"
    
    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,  #якщо кошик видалено, всі його CartItems видаляються автоматично
        related_name='items'
    )

    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    def get_subtotal(self):
        return self.product.price * self.quantity


    
class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Очікує обробки'),
        ('processing', 'В обробці'),
        ('shipped', 'Відправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Скасовано')
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True, 
        related_name='orders'
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.name}"
    
    def get_total(self):
        return sum(item.get_subtotal() for item in self.order_items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name='order_items'
    )


    product = models.ForeignKey(
            Product, 
            on_delete=models.SET_NULL, 
            null=True, 
            related_name='order_items'
        )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name if self.product else 'Видалений товар'}"
        
    def get_subtotal(self):
        return self.price * self.quantity
