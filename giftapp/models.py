from django.db import models

# Create your models here.

class customer(models.Model):
    cname=models.CharField(max_length=50)
    cadd=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=10)
    password=models.IntegerField()
    images=models.ImageField(upload_to='upload/', default="")

##############  added add to cart fuctionality
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/',default="")
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.customer.username}'s Cart"