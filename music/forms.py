from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:     # info about UserForm class
        model = User     # base model
        fields = ['username', 'email', 'password']