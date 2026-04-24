from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Unijeli ste neispravnu korisničku oznaku/lozinku"

    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')