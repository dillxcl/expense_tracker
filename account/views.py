from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm


## Library that handle login and logout authenticate
from django.contrib.auth import authenticate, login, logout

## the library to send the message to front once the request is done
from django.contrib import messages



# Create your views here.
# Login views  url : login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect username or password')
            return render(request,'user_login.html', {})
    return render(request,'user_login.html', {})

# Sign_up views url : sign_up
def sign_up(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    context = {'form':form}
    return render(request, 'user_sign_up.html', context)

# log_out views url : log_out
def log_out(request):
    logout(request)
    return redirect('login')