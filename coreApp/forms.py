from django.forms import ModelForm
from .models import Property_model

class ListingForm(ModelForm):
    class Meta:
        model = Property_model
     
        fields =[
            'name' ,
            'user' ,
            'location',
            'image',
           'rental_price',
            'security_deposit',
            # 'duration',
            'amenities',
            'status',
            'house_type',
            'size'
        ]
        