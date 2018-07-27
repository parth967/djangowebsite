from django import forms
from myapp.models import userdetail

class UserForm(forms.ModelForm):
    class Meta:
        model=userdetail
        fields="__all__"
