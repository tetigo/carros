from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    user_form = UserCreationForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        
    context={
        'user_form': user_form
    }
       
    return render(request, 'register.html', context)

def login_view(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('cars_list')
    context={
        'login_form': login_form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('cars_list')



