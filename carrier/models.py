from django.db import models

class Item(models.Model):
    item_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    item_name = models.CharField(max_length=200)
    sender_name = models.CharField(max_length=200)
    sender_no = models.FloatField(null=True, blank=True, default=0.0)
    receiver_name = models.CharField(max_length=200)
    receiver_no = models.FloatField(null=True, blank=True, default=0.0)
    pickup_place = models.CharField(max_length=300)
    dropoff_place = models.CharField(max_length=300)
    pickup_date = models.DateField(null=True, blank=True)
    delivery_price=models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.item_name + ' - ' + self.sender_name