from django.contrib.auth.models import User
from django.db import models


# # Create your models here.
# class Employees(models.Model):
#     emp_name = models.CharField(max_length=200)
#     emp_address = models.CharField(max_length=200)
#     emp_phonenmbr = models.IntegerField


class Bookstoredb(models.Model):
    Book_name = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Price = models.DecimalField(decimal_places=2, max_digits=5)
    image_url = models.CharField(max_length=5000)
    Book_availability = models.BooleanField(default=False)
    Type = models.CharField(max_length=200,null=True)
    Language = models.CharField(max_length=200,null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Bookstoredb)
    total_price = models.DecimalField(max_digits=10,decimal_places=5)
class Cartitems(models.Model):
    book = models.ForeignKey(Bookstoredb,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.Price * self.quantity


