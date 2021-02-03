from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı")
    password = forms.CharField(min_length=5, max_length=20, label="Parola", widget= forms.PasswordInput)
    confirm = forms.CharField(min_length=5, label="Parolayı Doğrulayın", widget= forms.PasswordInput)
    email = forms.EmailField(min_length=6, max_length=50 , label="E-posta")
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")
        if (password) and (confirm) and (password != confirm):
            raise forms.ValidationError("Girdiğiniz parolalar aynı olmalıdır.")
        values = {
            "username" : username,
            "password" : password,
            "email" : email
        }
        return values
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı")
    password = forms.CharField(min_length=5, label="Parola", widget= forms.PasswordInput)

