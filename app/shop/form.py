from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=60)
    phone = forms.CharField()
