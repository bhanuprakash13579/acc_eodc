import re
from django import forms
from .models import Importer


def validate_gmail(value):
    if not re.match(r'^[\w\.-]+@gmail\.com$', value):
        raise forms.ValidationError("Please provide a valid Gmail address.")

class ImporterForm(forms.Form):
    importer_name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    license_number = forms.IntegerField()
    lic_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    bond_number = forms.IntegerField()
    gmail_id = forms.EmailField(validators=[validate_gmail])


class DateInput(forms.DateInput):
    input_type = 'date'

class ImporterForm(forms.ModelForm):
    class Meta:
        model = Importer
        fields = ['importer_name',
            'iec_code',
            'address',
            'license_number',
            'lic_date',
            'bond_number',
            'bond_date',
            'bond_amt_executed',
            'duty_saved',
            'items_imported',
            'gmail_id',
            'radio_choice',
            ]
        widgets = {
            'lic_date': forms.DateInput(),
            'is_eodc_produced': forms.HiddenInput,
            'is_dgft_ack_produced': forms.HiddenInput,
            'is_letter_issued': forms.HiddenInput,
            'is_scn_issued': forms.HiddenInput,
            'is_ph1_issued': forms.HiddenInput,
            'is_ph2_issued': forms.HiddenInput,
            'is_oio_issued': forms.HiddenInput,
            'is_paused': forms.HiddenInput,
            'is_closed': forms.HiddenInput,
        }
        radio_choice = forms.ChoiceField(
            choices=Importer.CHOICES,
            widget=forms.RadioSelect,
        )