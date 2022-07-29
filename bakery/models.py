from django.db import models
from django.contrib.auth.models import User
import uuid
#from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.

class Branch(models.Model):
    branch_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    branch_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.branch_name
    # def __str__(self):
    #     return str(self.id)


CATEGORY_CHOICES = (
    ('C', "Cake"),
    ('B', "Bread"),
    ('CK', "Cookies"),
)


class Product(models.Model):
    branch = models.ForeignKey(
        Branch, on_delete=models.SET_NULL, blank=True, null=True)
    # category = models.ForeignKey('Category',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    selling_price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    #flavour = models.CharField(max_length=100,default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg', default="1")

    def __str__(self):
        return str(self.title)
    # def __str__(self):
    #     return str(self.id)


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

#     def __str__(self):
#         return self.name


class Customer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.TextField(blank=True, null=True, max_length=10)
    email = models.EmailField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return str(self.id)


class Payment(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ManyToManyField(Product)
    amount = models.IntegerField()
    payment_status = [
        ('paid', 'paid'),
        ('due', 'due')
    ]
    status = models.CharField(max_length=4, choices=payment_status)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.created)

    # def __str__(self):
        # return str(self.id)


class Cart(models.Model):
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.product)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

    # def __str__(self):
    #     return str(self.id)


class OrderPlaced(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
        ('Cancel', 'Cancel')
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price
