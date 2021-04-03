from django import forms
from .models import Cardata


# creating a form
class CardataForm(forms.ModelForm):
    class Meta:
        model = Cardata
        fields ='__all__'
    c_company= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'some_class ml-4 mt-4 btn ayush',
				   'id':'some_id'}))
    c_name= forms.CharField(
                           widget= forms.TextInput
                           (attrs={'class':'some_class',
                                   'type':'text',
				   'id':'some_id'}))
    c_price = forms.CharField(
        widget=forms.TextInput
        (attrs={'class': 'some_class',
                'type': 'text',
                'id': 'some_id'}))
