from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.core import validators

# class userlogin(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput)
#

class contactform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField(widget=forms.TextInput)
    message=forms.CharField(widget=forms.Textarea)

class userregistrationform(UserCreationForm):
    first_name=forms.CharField()
    last_name = forms.CharField()
    email=forms.EmailField()
    phone=forms.CharField(widget=forms.NumberInput)
    address=forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields= ['username','password1','password2','first_name','last_name','email','phone','address']


#payment form for user
class payform(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    amount=forms.CharField(widget=forms.NumberInput)





