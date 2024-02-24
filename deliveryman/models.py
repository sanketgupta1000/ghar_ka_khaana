from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class DeliveryMan(User):

    # Delivery man status sawing that he/she are available for delivery or not 
    status = models.CharField(max_length=10,default="inactive")

    #how many order he/she accepted(max 5)
    order_count = models.IntegerField(default=0)

class Delivery(models.Model):
    #order for this delivery
    order = models.ForeignKey(OrderSummary,on_delete=models.CASCADE)

    #deliveryman for this delivery
    delivery_man= models.ForeignKey(DeliveryMan,on_delete=models.CASCADE)

    #delivery accept time
    accepted_time_stamp =models.DateTimeField()

    #devivered time
    delivered_time_stamp=models.DateTimeField()
