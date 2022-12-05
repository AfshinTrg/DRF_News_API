from django import forms
from django.core.exceptions import ValidationError


class PanelForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and (username != 'demo'):
            raise ValidationError("Username Doesn't Exist, Please check again")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password and (password != 'demo'):
            raise ValidationError("Password is wrong, Please check again")
        return password

