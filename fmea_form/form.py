from django import forms 
from django.forms import ModelForm
from fmea_form.models import FmeaRegister, FmeaProcess

choices=(
    ("10","More than once per day"),
    ("9","Once every 3-4 days"),
    ("8","Once Every week")
)

class DateInput(forms.DateInput):
    input_type = 'date'

class FmeaForm1(forms.ModelForm):
    class Meta:
        model =FmeaRegister
        fields="__all__"
        widgets={
            'date':DateInput(),
            'revisedDate':DateInput(),
        }

class FmeaForm2(forms.ModelForm):
    class Meta:
        model =FmeaProcess
        fields="__all__"