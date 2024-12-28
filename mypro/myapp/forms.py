from django import forms
from .models import NewUser,Customer


class CustomerRegistration(forms.ModelForm):    
    class Meta:
        model = Customer
        fields =['name','lname','mobile']
        Widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
        }