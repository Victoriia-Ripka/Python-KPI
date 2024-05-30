# myapp/forms.py
from django import forms
import datetime

class ForecastForm(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    esize = forms.IntegerField(label='Engine size', min_value=1, max_value=10, widget=forms.NumberInput(attrs={'step': 0.1, 'value': 3.0}))
    power = forms.IntegerField(label='Horsepower', min_value=50, max_value=500, widget=forms.NumberInput(attrs={'step': 5, 'value': 185}))
    latlaunch = forms.DateField(label='Latest Launch Year', input_formats='date', widget=forms.DateInput())
    

    # email = forms.EmailField()
    # car_model = forms.ModelChoiceField(queryset=Car.objects.all())
    # comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
