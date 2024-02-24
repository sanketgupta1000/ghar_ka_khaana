from django.db import models
from django.db.models import Model
from foodie.models import Foodie
from kitchen.models import Tiffin
from django.core.validators import MinValueValidator

# model defination of "Order Summary"
class OrderSummary(models.Model):

    # foreign key of user to determine 'By whom order is make place'
    foodie = models.ForeignKey(Foodie, on_delete=models.CASCADE)

    # current status of order
    status = models.CharField(max_length = 50, default="ip", choices = {"ip":"In Progress","done":"Delivered"}) 

    # total price of order
    total_price = models.IntegerField()

    # time taken for taking order
    time_stamp = models.DateTimeField()


# model defination of ordered_tiffin
class OrderedTiffin(models.Model):

    # foreign key of order & tiffin to determine "which order contains which tiffin"
    order = models.ForeignKey(OrderSummary, on_delete=models.CASCADE)
    tiffin = models.ForeignKey(Tiffin, on_delete=models.CASCADE)

    # to determine no of tiffin(s) in current order
    quantity = models.PositiveSmallIntegerField(validators = [MinValueValidator(1)])
