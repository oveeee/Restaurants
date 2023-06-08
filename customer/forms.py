from django.contrib.auth.forms import forms
from customer.models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =[
            'full_name',
            'number',
            'user'
        ]