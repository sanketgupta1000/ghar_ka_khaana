from django.shortcuts import render, redirect
from .forms import KitchenCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from user.views import logout_required

# Create your views here.
def kitchen_login_required(request):
    user = request.user
    if not (user.is_authenticated and user.is_foodie):
        return redirect('foodie:login')
    else:
        return None

def index(request):
    response = kitchen_login_required(request)
    if response is not None:
        return response
    return render(request, 'kitchen/index.html')

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
            return redirect("kitchen:login_view")
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
