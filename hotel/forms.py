from django import forms

from hotel.models import BokkingRoom, ServiceHotel


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = BokkingRoom
        fields = ['date_arrival', 'date_departure', 'desc']
        widgets = {
            'desc': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'date_arrival': DateInput(),
            'date_departure': DateInput(),
        }
        # exclude = ('user',)

class ServiceHotelForm(forms.ModelForm):
    class Meta:
        model = ServiceHotel
        fields = ["mark"]
        widgets = {
            "type": forms.IntegerField()
        }