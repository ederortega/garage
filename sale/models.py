from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=180)
    contact = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=180)
    contact = models.CharField(max_length=30, blank=True)
    payment_method = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=180)
    category = models.ForeignKey("sale.Category", on_delete=models.CASCADE)
    value = models.FloatField()
    image_link = models.URLField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


class Delivery(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '({})-{}'.format(self.id, self.creation_date)


class DeliveryItem(models.Model):
    delivery = models.ForeignKey("sale.Delivery", on_delete=models.CASCADE)
    item = models.IntegerField()
    sell_value = models.FloatField()
    percentage = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return '{} - {}'.format(self.delivery, self.item)


class Sale(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '({})-{}'.format(self.id, self.creation_date)


class SaleItem(models.Model):
    sale = models.ForeignKey("sale.Sale", on_delete=models.CASCADE)
    value = models.FloatField()
    expense = models.FloatField()
    expense_description = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.sale, self.id)
