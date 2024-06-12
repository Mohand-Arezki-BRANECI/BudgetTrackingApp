from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    logged_user = request.user
    data = User.objects.all()
    
    user_exists = data.filter(user_email=logged_user.email).exists()

    if user_exists:
        return redirect('gestion')  # Change 'management_page' to your actual URL name
    
    return render(request, 'home.html')

def insert_user(request):
    if request.method=="POST":
        user_first_name = request.POST.get('first_name')
        user_last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        print(user_email,user_first_name,user_last_name,user_type)
        query = User(user_first_name = user_first_name, user_last_name = user_last_name, user_email = user_email, user_type = user_type)
        query.save()
    # redirecting to home after persistance
    return render(request, 'home.html')

def gestion(request):
    return render(request, 'gestion.html')

def choose_user_type(request):
    return render(request, 'usertype.html')


def redirect_after_choose_user_type(request):
    return redirect(request,'home')
