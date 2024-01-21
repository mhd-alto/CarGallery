from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from products.models import *
from .forms import UserRegistrationForm,CompanyForm
from .models import Company
from products.filters import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'],
                                    )
            login(request,user)
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    context = {"user_form": user_form}
    return render(request, "registration/register.html", context)

    
def index(request):
    try:
        company = Company.objects.filter(user=request.user).first()
    except:
        company = None
    cars = Car.objects.all().order_by("-created")[:6]
    carParts = CarPart.objects.all().order_by("-created")[:6]
    offers = Offers.objects.all().order_by("-created")[:6]
    return render(request,'index.html',context={"company":company,'cars':cars,'carParts':carParts,"offers":offers})

def registerCompany(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CompanyForm(request.POST,request.FILES)
            if form.is_valid():
                new_form =  form.save(commit=False)
                new_form.user = request.user
                if request.FILES:
                    form.statement = request.FILES["statement"]
                    form.payment_note_image = request.FILES["payment_note_image"]
                    form.company_logo = request.FILES["company_logo"]
                new_form.save()
                return redirect('index')
        else:
            form = CompanyForm()
        return render(request,'makeProfile.html',context={'form':form})
    else:
       return redirect('login')

@login_required(login_url='login')
def editCompany(request):
    company_to_edite = get_object_or_404(Company,user=request.user)
    if request.method == "POST":
        form = CompanyForm(request.POST,request.FILES,instance=company_to_edite)
        if form.is_valid():
            if request.FILES:
                form.statement = request.FILES["statement"]
                form.payment_note_image = request.FILES["payment_note_image"]
                form.company_logo = request.FILES["company_logo"]
            form.save()
            return redirect('index')
    else:
        form = CompanyForm(instance=company_to_edite)
    return render(request,'editeProfile.html',context={'form':form,'company':company_to_edite})

def companies(request):
    companies = Company.objects.all().order_by('-id')
    companyFilter = CompanyFilter(request.POST,queryset=companies)
    companies =companyFilter.qs
    return render(request,'companies.html',{"companies":companies,'companyFilter':companyFilter})        


