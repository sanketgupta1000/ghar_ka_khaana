from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from .models import *
from .forms import *
from user.views import logout_required
from kitchen.models import Tiffin

# Create your views here.
def foodie_login_required(request):
    user = request.user
    if not (user.is_authenticated and user.is_foodie):
        return redirect('foodie:login')
    else:
        return None

def index(request):
    response = foodie_login_required(request)
    if response is not None:
        return response

    if request.method=='GET':
        # will show available tiffins

        # getting all tiffins
        tiffins = Tiffin.objects.all()

        # render the template
        return render(request, 'foodie/index.html', {'tiffins':tiffins})

def register(request):
    response = logout_required(request)
    if response is not None:
        return response

    if request.method == 'POST':
        form = FoodieCreationForm(request.POST)

        if form.is_valid():
            user = form.save(False)
            user.is_foodie = True
            user.save()
            return redirect('foodie:login')
    else:
        form = FoodieCreationForm()
    return render(request, 'foodie/register.html', {
        'form' : form,
    })
        

def login_request(request):
    response = logout_required(request)
    if response is not None:
        return response
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None and user.is_foodie==True:
                login(request,user)
                return redirect('foodie:index')
    else:
        form = AuthenticationForm()


    return render(request, 'foodie/login.html',{
        'form' : form,
    })