from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from products.views import *

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register_company/',views.registerCompany,name='registerCompany'),
    path('edit_Company/',views.editCompany,name='editCompany'),
    path('manage_cars/',manage_cars,name='manage_cars'),
    path('manage_offer/',manage_offers,name='manage_offers'),
    path('manage_carPart/',manage_carPart,name='manage_carPart'),
]