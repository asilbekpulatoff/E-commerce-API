from django.db import models
from accounts.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='category/images', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='childs', on_delete=models.PROTECT, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(Category, related_name='products_category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images', blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class ProductAdd(models.Model):
    product_add = models.ForeignKey(Product,related_name='products', on_delete=models.CASCADE)
    quantity_add = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # Buyurtma qilinganda total_price-ni avtomatik hisoblash
        product_quantity = self.product_add
        product_quantity.quantity += self.quantity_add
        product_quantity.save()
        super().save(*args, **kwargs)


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=250)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} by {self.user_profile.user.username}"

    def save(self, *args, **kwargs):
        # Buyurtma qilinganda total_price-ni avtomatik hisoblash
        self.total_price = self.quantity * self.product.price
        product = self.product
        product.quantity -= self.quantity
        product.save()
        super().save(*args, **kwargs)

        
 
