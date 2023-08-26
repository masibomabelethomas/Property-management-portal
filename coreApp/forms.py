from django.forms import ModelForm
from .models import Property_model

class ListingForm(ModelForm):
    class Meta:
        model = Property_model

        fields =[

            "name" ,
            "address" ,
            "size" ,
            "num_rooms",
            "amenities" ,
            "rental_price" ,
            "status" ,
        ]