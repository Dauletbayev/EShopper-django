from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission


# Create your models here.

class CategoryModel(models.Model):
    category_title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    category_photo = models.FileField(upload_to='product_images')

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

class ProductModel(models.Model):
    product_title = models.CharField(max_length=50)
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_description = models.TextField()
    product_count = models.IntegerField()
    product_price = models.FloatField()
    product_image = models.FileField(upload_to='product_images')
    product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None'),
    )
    user_gender = models.CharField(max_length=7, choices=GENDERS, default='None')
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    objects = UserManager()

class CartModel(models.Model):
    user_id = models.IntegerField()
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_product_count = models.IntegerField()
    user_add_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'User cart'
        verbose_name_plural = 'User carts'

