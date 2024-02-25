from django.shortcuts import render, redirect
from .forms import KitchenCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from user.views import logout_required
from .models import Tiffin, TiffinItem, TiffinItemCategory, Kitchen
from datetime import date, datetime

# Create your views here.
def kitchen_login_required(request):
    user = request.user
    if not (user.is_authenticated and user.is_kitchen):
        return redirect('kitchen:login')
    else:
        return None

def index(request):
    response = kitchen_login_required(request)
    if response is not None:
        return response
    
    if request.method=='GET':
        # fetch tiffin from DB
        tiffins = Tiffin.objects.filter(kitchen=request.user)
        # to template
        

        return render(request, "kitchen/index.html", {'tiffins': tiffins})
    else:
        # request via post
        # getting params
        bread = request.POST.get('bread')
        bread_qty = request.POST.get('bread-qty')
        veg1 = request.POST.get('veg1')
        veg1_qty = request.POST.get('veg1-qty')
        veg2 = request.POST.get('veg2')
        veg2_qty = request.POST.get('veg2-qty')
        dalrice = request.POST.get('dalrice')
        dalrice_qty = request.POST.get('dalrice-qty')
        price = request.POST.get('price')
        maxqty = request.POST.get('max-qty')
        # creating tiffin
        tiffin = Tiffin(kitchen=Kitchen.objects.get(id=request.user.id), price=price, date=date.today(), end_time=datetime.now().time(), max_quantity_available=maxqty)
        # save tiffin
        tiffin.save()

        # creating tiffin item objects and saving
        tiffinitem1 = TiffinItem(category=TiffinItemCategory.objects.get(name='bread'), tiffin=tiffin, name=bread, qty_per_tiffin=bread_qty)
        tiffinitem2 = TiffinItem(category=TiffinItemCategory.objects.get(name='veg1'), tiffin=tiffin, name=veg1,  qty_per_tiffin=veg1_qty)
        tiffinitem3 = TiffinItem(category=TiffinItemCategory.objects.get(name='veg2'), tiffin=tiffin, name=veg2,  qty_per_tiffin=veg2_qty)
        tiffinitem4 = TiffinItem(category=TiffinItemCategory.objects.get(name='dalrice'), tiffin=tiffin, name=dalrice, qty_per_tiffin=dalrice_qty)

        tiffinitem1.save()
        tiffinitem2.save()
        tiffinitem3.save()
        tiffinitem4.save()


        # redirect to same page only
        return redirect('kitchen:index')


def register_view(request):
    response = logout_required(request)
    if response is not None:
        return response

    if request.method=='POST':
        # user has submitted form
        # get filled form as form object
        form = KitchenCreationForm(request.POST)
        if form.is_valid():
            # valid
            # set into user model and get model object
            user = form.save(False)
            # set the user type
            user.is_deliveryman = False
            user.is_foodie = False
            user.is_kitchen = True
            # save
            user.save()
            # rendirect to kitchen login
            return redirect("kitchen:login")
    else:
        form = KitchenCreationForm()
    # in case of request by get, or invalid form filled, show form
    return render(request, "kitchen/register.html", {'form': form})

# function to help in login
def login_view(request):
    response = logout_required(request)
    if response is not None:
        return response

    if request.method=='POST':
        # user submitted the login form
        # getting user filled data as form
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # valid form filled
            # getting username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # authenticating
            user = authenticate(username=username, password=password)
            if user is not None and user.is_kitchen==True:
                # valid username and password
                # logging in
                login(request, user)
                return redirect("kitchen:index")
    else:
        # user requested page via get
        # create empty form to show
        form = AuthenticationForm()
    # if the user filled invalid form, or if username/password incorrect, or if user requested via get, show him form
    return render(request, "kitchen/login.html", {'form': form})