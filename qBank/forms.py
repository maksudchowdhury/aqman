from django import forms
from django.core.validators import RegexValidator

# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# alphanumeric = RegexValidator(r'^[a-zA-Z0-9._\-+]+$', 'Only alphanumeric characters are allowed.')
# emailInitialValidator = RegexValidator(r'/[^a-z0-9.\-+_]/gi', 'Only alphanumeric characters and . _ + - are allowed.')
# passwordValidator = RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{8,}$', '1 uppercase, 1 lowercase, 1 digit, 1 special character required. Minimum 8 characters.')

class signUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    # email_initial = forms.CharField(max_length=200, required=True, validators=[emailInitialValidator])
    email_initial = forms.CharField(max_length=200, required=True)
    institution_id = forms.CharField(max_length=100, required=True)
    otpcode = forms.CharField(max_length=8, required=True, widget=forms.TextInput(attrs={'pattern':'[A-Za-z0-9]+'}) )  
    # otpcode = forms.CharField(max_length=8, required=True)  
    # password = forms.CharField(max_length=100,required=True, widget=forms.PasswordInput(), validators=[passwordValidator])
    # confirm_password = forms.CharField(max_length=100,required=True, widget=forms.PasswordInput(), validators=[passwordValidator])
    password = forms.CharField(max_length=100,required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=100,required=True, widget=forms.PasswordInput())