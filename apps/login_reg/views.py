from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.
def index(request):
    return render(request, 'login_reg/login_reg.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        check_email = User.objects.filter(email=request.POST["email"])
        if check_email:
            errors["email"] = "Email already in use"
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return redirect('/')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        request.session["user_id"] = user.id
        return redirect('/dashboard') ### /dashboard, not index or welcome, please note
    return redirect('/')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
        except:
            messages.error(request, "Email invalid")
            return redirect('/')
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, "Password invalid")
            return redirect('/')
        request.session["user_id"] = user.id
        return redirect('/dashboard') ### /dashboard, not index or welcome, please note
    else:
        return redirect('/')
    
def logout(request):
    request.session.clear()
    return redirect('/')