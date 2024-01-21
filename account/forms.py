from django import forms
from django.contrib.auth.models import User
from .models import Company



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control form-control-sm "}))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class":"form-control form-control-sm "}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-control-sm "}))
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        help_texts = {
            'username': None,
        }

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["confirm_password"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["confirm_password"]

class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(label="Company name", widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    adderss = forms.CharField(label="Adderss", widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    company_phonenumber = forms.CharField(label="company phonenumber", widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    statement = forms.FileField(label="statement", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    payment_note_image = forms.FileField(label="Payment Note Image", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    company_services = forms.CharField(label="Company Services",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
    company_logo = forms.FileField(label="Company Logo", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    class Meta:
        model = Company
        fields = ("company_name","adderss","company_phonenumber","statement","payment_note_image",
        "company_services","company_logo","is_active")