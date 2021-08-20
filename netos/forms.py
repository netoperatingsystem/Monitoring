from django import forms
from .models import Labipaddress
from .models import Device

class NowyLabipaddressForm(forms.ModelForm):
    class Meta:
        model = Labipaddress
        fields = '__all__'


