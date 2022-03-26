from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Adress(models.Model):
    street_and_number = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.street_and_number}, {self.postal_code}, {self.city}, {self.country}'



class Product(models.Model):
    CATEGORY_T = 'T'
    CATEGORY_P = 'P'
    CATEGORY_B = 'B'
    CATEGORY_CHOICES = [
        (CATEGORY_T, 'Trenerki'),
        (CATEGORY_P, 'Pizami'),
        (CATEGORY_B, 'Bluzi')
    ]

    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_XL = 'XL'

    SIZE_CHOICES = [
        (SIZE_S, 'S'),
        (SIZE_M, 'M'),
        (SIZE_L, 'L'),
        (SIZE_XL, 'XL')
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    price = models.FloatField()
    customer = models.ManyToManyField('Customer', through='CustomerProduct')
    
    # def __str__(self) -> str:
    #     return f'{self.name}, {self.category}, {self.price} '

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    credit_card = models.CharField(max_length=16, validators=[MinLengthValidator(16)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_adress = models.OneToOneField(Adress, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through= 'CustomerProduct', related_name='products')

    # def __str__(self) -> str:
    #     return f'{self.first_name} {self.last_name}'


class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)