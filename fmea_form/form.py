from django import forms 
from django.forms import ModelForm
from fmea_form.models import FmeaRegister, FmeaProcess



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