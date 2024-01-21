import django_filters
from . models import Car,CarPart,Offers
from account.models import Company
from django.db.models import Q
from django import forms

class CarFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(label='search',method='filter_search',widget=forms.widgets.TextInput(attrs={'placeholder': 'Search Cars & details ','class':'form-control'}))
    price = django_filters.NumberFilter(label='price',field_name='price',lookup_expr='lte',widget=forms.widgets.NumberInput(attrs={'placeholder': 'Search price','class':'form-control'}))
    
    def filter_search(self,queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )

    class Meta:
        model = Car
        fields = ['search','price']


class CarPartFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(label='search',method='filter_search',widget=forms.widgets.TextInput(attrs={'placeholder': 'Search Part ','class':'form-control'}))
    price = django_filters.NumberFilter(label='price',field_name='price',lookup_expr='lte',widget=forms.widgets.NumberInput(attrs={'placeholder': 'Search price','class':'form-control'}))
    
    def filter_search(self,queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )

    class Meta:
        model = CarPart
        fields = ['search','price']


class OfferFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(label='search',method='filter_search',widget=forms.widgets.TextInput(attrs={'placeholder': 'Search Offers ','class':'form-control'}))
    price = django_filters.NumberFilter(label='price',field_name='price',lookup_expr='lte',widget=forms.widgets.NumberInput(attrs={'placeholder': 'Search price','class':'form-control'}))
    
    def filter_search(self,queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )

    class Meta:
        model = Offers
        fields = ['search','price']


class CompanyFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(label='search',method='filter_search',widget=forms.widgets.TextInput(attrs={'placeholder': 'Search Companies ','class':'form-control'}))
    
    def filter_search(self,queryset, name, value):
        return queryset.filter(
            Q(company_name__icontains=value) |
            Q(company_services__icontains=value)
        )

    class Meta:
        model = Company
        fields = ['search']


