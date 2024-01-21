from django.urls import path
from . import views

urlpatterns = [
    path('cars/',views.car_list,name='car_list'),
    path('add_car/',views.add_car,name='add_car'),
    path('car_details/<int:car_id>',views.car_details,name='car_details'),
    path('edit_car/<int:car_id>',views.edit_car,name='edit_car'),
    path('delete_car/<int:car_id>',views.deleteCar,name='deleteCar'),
    path('addCarComment/<int:car_id>',views.addCarComment,name='addCarComment'),
    #car_parts______________________________________
    path('carParts/',views.carPart_list,name='carPart_list'),
    path('add_carParts/',views.add_carPart,name='add_carPart'),
    path('carPart_details/<int:carPart_id>',views.carPart_details,name='carPart_details'),
    path('edit_carPart/<int:carPart_id>',views.edit_carPart,name='editPart_car'),
    path('delete_carPart/<int:part_id>',views.deleteCarPart,name='deleteCarPart'),
    path('addCarPartComment/<int:carPart_id>',views.addCarPartComment,name='addCarPartComment'),
    #offers_________________________________________
    path('offers/',views.offers_list,name='offers_list'),
    path('add_offer/',views.add_offer,name='add_offer'),
    path('offer_details/<int:offer_id>',views.offer_details,name='offer_details'),
    path('edit_offer/<int:offer_id>',views.edit_offer,name='edit_offer'),
    path('delete_offer/<int:offer_id>',views.deleteOffer,name='deleteOffer'),
    path('addOfferComment/<int:offer_id>',views.addOfferComment,name='addOfferComment'),

    # path('test/',views.recBrandParts,name='test'),


]