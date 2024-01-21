from django import forms
from djmoney.forms.widgets import MoneyWidget
from .models import *



class CarForm(forms.ModelForm):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    description = forms.CharField(label="description",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
    main_image = forms.FileField(label="main_image", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(),widget=forms.Select(attrs={"class":"form-control form-control-sm "}))
    color = forms.ModelChoiceField(queryset=Color.objects.all(),widget=forms.Select(attrs={"class":"form-control form-control-sm "}))
    
    class Meta:
        model = Car
        fields = ['title','main_image','description','price','color','brand']
    

class CarCommentForm(forms.ModelForm):
    text = forms.CharField(label="comment",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
   
    class Meta:
        model = CarComment
        fields = ['text']

class CarPartForm(forms.ModelForm):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={"class":"form-control form-control-sm"}))
    description = forms.CharField(label="description",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
    image = forms.FileField(label="main_image", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(),widget=forms.Select(attrs={"class":"form-control form-control-sm "}))
    
    class Meta:
        model = CarPart
        fields = ['title','image','description','price','brand']

class CarPartCommentForm(forms.ModelForm):
    text = forms.CharField(label="comment",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
   
    class Meta:
        model = CarPartComment
        fields = ['text']


class OfferForm(forms.ModelForm):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={"class":"form-control form-control-sm "}))
    description = forms.CharField(label="description",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
    image = forms.FileField(label="main_image", widget=forms.FileInput(attrs={"class":"form-control form-control-sm "}))
    
    class Meta:
        model = Offers
        fields = ['title','image','description','price']
    

class OfferCommentForm(forms.ModelForm):
    text = forms.CharField(label="comment",widget=forms.Textarea(attrs={"class":"form-control form-control-sm "}))
   
    class Meta:
        model = OffersComment
        fields = ['text']