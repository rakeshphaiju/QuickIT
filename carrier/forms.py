from django.forms import ModelForm
from .models import Item

class ItemForm(forms.ModelForm):


    class Meta: 
        model = Item
        #fields = ("item_image", "item_name", "sender_name", "sender_no", "receiver_name", "receiver_no", "pickup_place", "dropoff_place", "pickup_date", "delivery_price",]
        fields = '_all_'