from django import forms
from .models import Labipaddress


class NowyLabipaddressForm(forms.ModelForm):
    class Meta:
        model = Labipaddress
        fields = '__all__'


