from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

class Item(models.Model):
    item_name = models.CharField(max_length=200, default='')
    sender_name = models.CharField(max_length=200, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    sender_no = models.CharField(max_length=17, null=True, blank=True)
    receiver_name = models.CharField(max_length=200, default='')
    receiver_no = models.CharField(max_length=17, default='')
    pickup_place = models.CharField(max_length=300, default='')
    dropoff_place = models.CharField(max_length=300, default='')
    pickup_date = models.DateField(null=True, blank=True)
    delivery_price=models.FloatField(null=True, blank=True, default=0.0)
    item_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def get_absolute_url(self):
        return reverse('carrier:item-list')

    def __str__(self):
        return self.item_name + ' - ' + self.sender_name

 