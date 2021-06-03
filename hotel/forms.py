from django import forms

from hotel.models import BokkingRoom, ServiceHotel


class DateInput(forms.DateInput):  # Записать
    input_type = 'date'  # Записать


class BookingForm(forms.ModelForm):
    class Meta:
        model = BokkingRoom
        fields = ['date_arrival', 'date_departure', 'desc']
        widgets = {
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'date_arrival': DateInput(),  # Записать
            'date_departure': DateInput(),
        }
        # exclude = ('account',)


class ServiceHotelForm(forms.Form):
    mark = forms.IntegerField(min_value=1, max_value=5, initial=5)
    # class Meta:
    #     model = ServiceHotel
    #     fields = ['mark']
    #     widgets = {
    #         'mark': forms.IntegerField(max_value=1)
    #     }
