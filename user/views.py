from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def logout_required(request):
    if request.user.is_authenticated:
        if request.user.is_foodie:
            return redirect('foodie:index')
        elif request.user.is_kitchen:
            return redirect('kitchen:index')
        elif request.user.is_deliveryman:
            return redirect('deliveryman:index')
    else:
        return None

def landingpage_view(request):
    return render(request, 'landingpage.html', {})

def logout_request(request):
    logout(request)
    return redirect('landingpage')
        