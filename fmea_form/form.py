from django import forms 
from django.forms import ModelForm, TextInput, EmailInput
from fmea_form.models import FmeaRegister, FmeaProcess



class DateInput(forms.DateInput):
    input_type = 'date'

class FmeaForm1(forms.ModelForm):
    class Meta:
        model =FmeaRegister
        fields="__all__"
        widgets={
            'process':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Process Name'
                }),
            'preparedBy':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Prepared By'
                }),
            'responsible':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Responsible'
                }),
            'date':DateInput(attrs={
                'class': "form-control mb-2",
                }),
            'revisedDate':DateInput(attrs={
                'class': "form-control mb-2",
                }),
        }

class FmeaForm2(forms.ModelForm):
    class Meta:
        model =FmeaProcess
        fields="__all__"
        widgets={
            'fmeaRegister':forms.Select(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Process'
                }),
            'processStep':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Process Step'
                }),
            'processType':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Process Type'
                }),
            'potentialFaliureMode':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Potential Failure Mode'
                }),
            'potentialFailureEffect':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Potential Failure Effect'
                }),
            'severity':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Severity'
                }), 
            'potentialCause':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Potential Cause'
                }),
            'occurence':forms.Select(attrs={
                'class': "form-control mb-2",
            }), 
            'currentControls':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Current Controls'
                }), 
            'detection':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Detection'
                }), 
            'actionRecommended':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Action Recommended'
                }),
            'responsiblePerson':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Responsible Person'
                }),
            'actionTaken':TextInput(attrs={
                'class': "form-control mb-2",
                'placeholder': 'Action Taken'
                }),   
        }