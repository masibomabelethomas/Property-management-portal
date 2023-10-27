from django.forms import ModelForm
from .models import Property_model
class ListingForm(ModelForm):
    class Meta:
        model = Property_model
        fields = '__all__'
        # fields =[
        #     'property_name',
        #     'user',
        #     'location',
        #     'image',
        #    'rental_price',
        #     'security_deposit',
        #     'status',
        #     'house_type',
        #     'size'
        # ]
        