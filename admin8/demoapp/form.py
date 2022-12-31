from django import forms

from demoapp.models import Mobilephone

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobilephone
        fields = '__all__'
