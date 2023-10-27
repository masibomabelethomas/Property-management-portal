from django import forms

class BookingForm(forms.Form):
    check_in_date = forms.DateField(widget=forms.SelectDateWidget)
    check_out_date = forms.DateField(widget=forms.SelectDateWidget)
    number_of_guests = forms.IntegerField()
