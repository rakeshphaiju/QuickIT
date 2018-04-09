from django.db import models
from django.core.validators import RegexValidator

class Item(models.Model):
    item_image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    item_name = models.CharField(max_length=200)
    sender_name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    sender_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    receiver_name = models.CharField(max_length=200)
    receiver_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    pickup_place = models.CharField(max_length=300)
    dropoff_place = models.CharField(max_length=300)
    pickup_date = models.DateField(null=True, blank=True)
    delivery_price=models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.item_name + ' - ' + self.sender_name