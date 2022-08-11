from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from main.models import User

# Create your views here.


def register(request):
    registered = False
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            # return redirect('/')
    else:
        form = RegisterForm()

    username = request.session.get('username', 0)
    # return redirect("/login")
    return render(request, 'register/register.html', {'form': form, 'registered': registered, 'username': username})


def user_login(request):
    logged = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # result = "Hello " + username
            request.session['username'] = username
            username = request.session.get('username', 0)
            logged = True
            # redirect('/')
            return render(request, "registration/login.html", {'login_result': result, 'username': username})
        else:
            print("You can't login.")
            print("Username: {} and password: {}".format(username, password))
            login_result = "Username or password is incorrect!"
            logged = False
            return render(request, "registration/login.html", {'login_result': login_result})
    else:
        return render(request, "registration/login.html", {'last_visit': last_visit})


@login_required
def user_logout(request):
    logout(request)
    result = "You're logged out. You can login again."
    return render(request, "registration/login.html", {'logout_result': result, })
