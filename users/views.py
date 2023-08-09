from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('crud:home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('crud:home')
        
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request,"users/login-register.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('crud:home')
    form = MyUserCreationForm()
    for field in form:
        print(field.label)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('crud:home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request,"users/login-register.html", {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('crud:home')