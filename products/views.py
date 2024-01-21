from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,HttpResponse
from .models import *
from account.models import Company
from .forms import *
from django.urls import reverse_lazy,reverse
# from django.db.models import Q
import django_filters
from .filters import CarFilter,CarPartFilter,OfferFilter 
from django.core.exceptions import PermissionDenied


def recBrandCars(request):
    liked_brands=[]
    for car in Car.objects.all():
        for like in car.likes.all():
            print(like.username)
            if (like == request.user):
                liked_brands.append(car.brand)
    counter = 0
    req_brands = None
    for brand in liked_brands:
        curr_frequency = liked_brands.count(brand)
        if curr_frequency>counter:
            counter =curr_frequency
            req_brands = brand
    return req_brands

def recBrandParts(request):
    liked_brands=[]
    for i in request.user.parts_likes.all():
        print(i)
        liked_brands.append(i.brand)
    counter = 0
    req_brands = None
    for brand in liked_brands:
        curr_frequency = liked_brands.count(brand)
        if curr_frequency>counter:
            counter =curr_frequency
            req_brands = brand

    return req_brands



def car_list(request):
    recCars = None
    brand = None
    if request.user.is_authenticated:
       brand =  recBrandCars(request)
       recCars = Car.objects.filter(brand=brand).order_by('-updated')[:6]
    cars = Car.objects.all().order_by('-updated')
    cars = cars.exclude(brand=brand)
    brands = Brand.objects.all()
    colors = Color.objects.all()
    carFilter = CarFilter(request.POST,queryset=cars)
    cars = carFilter.qs
    if request.method == 'POST':
        brand = request.POST.get('brand','none')
        color = request.POST.get('color','none')
        if brand !='none' and color != 'none':
            cars = Car.objects.filter(brand=brand,color=color)
        elif brand !='none':
            cars = Car.objects.filter(brand=brand).order_by('-updated')
        elif color != 'none':
            cars = Car.objects.filter(color=color).order_by('-updated')
    return render(request,'cars/cars_list.html',{'cars':cars,'carFilter':carFilter,'brands':brands,'colors':colors,'recCars':recCars})


            
def add_car(request):
    company = get_object_or_404(Company,user=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = get_object_or_404(Company,user=request.user)
            if request.FILES:
                new_form.main_image = request.FILES['main_image']
            new_form.save()
            return redirect('manage_cars')
    else:
        form = CarForm()
    return render(request,'cars\\add_car.html',{"form":form,'company':company})

def car_details(request,car_id):
    liked = False
    car = get_object_or_404(Car,pk=car_id)
    if request.user in car.likes.all():
        liked = True
    else:
        liked = False
    form = CarCommentForm()
    comment = CarComment.objects.filter(car=car)
    company = Company.objects.all()
    if request.method == "POST":
        if request.user in car.likes.all():
            car.likes.remove(request.user)
            liked = False
        else:
            car.likes.add(request.user)
            liked = True
    return render(request,'cars/car_details.html',{"car":car,"form":form,"comment":comment,'company':company,'liked':liked,"likesCount":car.likes.count})


def edit_car(request,car_id):
    company = get_object_or_404(Company,user=request.user)
    car = get_object_or_404(Car,pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            new_form = form.save(commit=False)
            if request.FILES:
                new_form.main_image = request.FILES['main_image']
            new_form.save()
            return redirect('manage_cars')
    else:
        form = CarForm(instance=car)
    return render(request,'cars\\edit_car.html',{"form":form,'car':car,'company':company})



def deleteCar(request,car_id):
    car = get_object_or_404(Car,pk=car_id)
    if request.user == car.author.user:
        car.delete()
    else:
        return HttpResponse('not same user')
    return redirect('manage_cars')


def addCarComment(request,car_id):
    car = get_object_or_404(Car,pk=car_id)
    if request.method == 'POST':
        form = CarCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.car = car
            new_form.save()
            return redirect('car_details',car_id)
    return redirect('car_details',car_id)




#________________________carParts_____________________

def carPart_list(request):
    recParts = None
    brand = None
    if request.user.is_authenticated:
       brand =  recBrandParts(request)
       recParts = CarPart.objects.filter(brand=brand).order_by('-updated')[:6]
    carParts = CarPart.objects.all().order_by('-updated')
    carPartFilter = CarPartFilter(request.POST,queryset=carParts)
    brands = Brand.objects.all()
    carParts =carPartFilter.qs
    companies = Company.objects.all()
    if request.method == 'POST':
        brand = request.POST.get('brand','none')
        if brand !='none':
            print(brand)
            carParts = CarPart.objects.filter(brand=brand).order_by('-updated')
    return render(request,'parts/carPart_list.html',{'carParts':carParts,'companies':companies,'carPartFilter':carPartFilter,'brands':brands,'recParts':recParts})

def add_carPart(request):
    company = get_object_or_404(Company,user=request.user)
    if request.method == 'POST':
        form = CarPartForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = get_object_or_404(Company,user=request.user)
            if request.FILES:
                new_form.image = request.FILES['image']
            new_form.save()
            return redirect('manage_carPart')
    else:
        form = CarPartForm()
    return render(request,'parts\\add_carPart.html',{"form":form,'company':company})

def carPart_details(request,carPart_id):
    carPart = get_object_or_404(CarPart,pk=carPart_id)
    if request.user in carPart.likes.all():
        liked = True
    else:
        liked = False
    form = CarPartCommentForm()
    comment = CarPartComment.objects.filter(carPart=carPart)
    company = Company.objects.all()
    if request.method == "POST":
        if request.user in carPart.likes.all():
            carPart.likes.remove(request.user)
            liked = False
        else:
            carPart.likes.add(request.user)
            liked = True
    return render(request,'parts/carPart_details.html',{"carPart":carPart,'form':form,'comment':comment,"company":company,'liked':liked,"likesCount":carPart.likes.count})

def edit_carPart(request,carPart_id):
    company = get_object_or_404(Company,user=request.user)
    carPart = get_object_or_404(CarPart,pk=carPart_id)
    if request.method == 'POST':
        form = CarPartForm(request.POST,request.FILES,instance=carPart)
        if form.is_valid():
            new_form = form.save(commit=False)
            if request.FILES:
                new_form.image = request.FILES['image']
            new_form.save()
            return redirect('manage_carPart')
    else:
        form = CarPartForm(instance=carPart)
    return render(request,'parts\\edit_carPart.html',{"form":form,'car':carPart,'company':company})

def deleteCarPart(request,part_id):
    carPart = get_object_or_404(CarPart,pk=part_id)
    if request.user == carPart.author.user:
        carPart.delete()
    else:
        return HttpResponse('not same user')
    return redirect('manage_carPart')


def addCarPartComment(request,carPart_id):
    carPart = get_object_or_404(CarPart,pk=carPart_id)
    if request.method == 'POST':
        form = CarPartCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.carPart = carPart
            new_form.save()
            return redirect('carPart_details',carPart_id)
    return redirect('carPart_details',carPart_id)
    

#________________________offers_______________
def offers_list(request):
    offers = Offers.objects.all().order_by('-updated')
    offersFilter = OfferFilter(request.POST,queryset=offers)
    offers =offersFilter.qs
    companies = Company.objects.all()
    return render(request,'offers/offer_list.html',{'offers':offers,'companies':companies,'offersFilter':
    offersFilter})

def add_offer(request):
    company = get_object_or_404(Company,user=request.user)
    if request.method == 'POST':
        form = OfferForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = get_object_or_404(Company,user=request.user)
            if request.FILES:
                new_form.image = request.FILES['image']
            new_form.save()
            return redirect('manage_offers')
    else:
        form = OfferForm()
    return render(request,'offers/add_offer.html',{"form":form,'company':company})

def offer_details(request,offer_id):
    offer = get_object_or_404(Offers,pk=offer_id)
    form = OfferCommentForm()
    comment = OffersComment.objects.filter(Offer=offer)
    company = Company.objects.all()
    return render(request,'offers/offer_details.html',{"offer":offer,'form':form,'comment':comment,'company':company})

def edit_offer(request,offer_id):
    company = get_object_or_404(Company,user=request.user)
    offer = get_object_or_404(Offers,pk=offer_id)
    if request.method == 'POST':
        form = OfferForm(request.POST,request.FILES,instance=offer)
        if form.is_valid():
            new_form = form.save(commit=False)
            if request.FILES:
                new_form.image = request.FILES['image']
            new_form.save()
            return redirect('manage_offers')
    else:
        form = OfferForm(instance=offer)
    return render(request,'offers/edit_offer.html',{"form":form,'offer':offer,'company':company})

def deleteOffer(request,offer_id):
    offer = get_object_or_404(Offers,pk=offer_id)
    if request.user == offer.author.user:
        offer.delete()
    else:
        return HttpResponse('not same user')
    return redirect('manage_offers')


def addOfferComment(request,offer_id):
    offer = get_object_or_404(Offers,pk=offer_id)
    if request.method == 'POST':
        form = OfferCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.Offer = offer
            new_form.save()
            return redirect('offer_details',offer_id)
    return redirect('offer_details',offer_id)
    
#_______________________Manage_Product___________________
def manage_cars(request):
    company = Company.objects.filter(user=request.user).first()
    cars = Car.objects.filter(author=company).order_by('-updated')
    carFilter = CarFilter(request.POST,queryset=cars)
    cars = carFilter.qs
    return render(request,'manage/manage_cars.html',context={'cars':cars,'carFilter':carFilter,'company':company})


def manage_offers(request):
    company = Company.objects.filter(user=request.user).first()
    offers = Offers.objects.filter(author=company).order_by('-updated')
    offersFilter = OfferFilter(request.POST,queryset=offers)
    offers =offersFilter.qs
    return render(request,'manage/manage_offers.html',context={'offers':offers,'offersFilter':offersFilter,'company':company})

def manage_carPart(request):
    company = Company.objects.filter(user=request.user).first()
    carPart = CarPart.objects.filter(author=company).order_by('-updated')
    carPartFilter = CarPartFilter(request.POST,queryset=carPart)
    carPart =carPartFilter.qs
    return render(request,'manage/manage_carPart.html',context={'carParts':carPart,'carPartFilter':carPartFilter,'company':company})

