from django import forms

class AddCow(forms.Form):
    user_input = forms.CharField(max_length=100)