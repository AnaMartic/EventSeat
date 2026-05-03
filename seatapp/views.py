from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import Event, Guest
from django.db.models import Q
from django.contrib.auth.models import User

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
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            error = "Unijeli ste neispravnu korisničku oznaku/lozinku"

    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def admin_dashboard(request):
    error = None

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            username = request.POST.get('username')
            password = request.POST.get('password')
            event_name = request.POST.get('event_name')
            event_date = request.POST.get('event_date')

            if Event.objects.filter(date=event_date).exists():
                error = "Odabrani datum je već zauzet."
            elif User.objects.filter(username=username).exists():
                error = "Korisnik već postoji."
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                Event.objects.create(
                    user=user,
                    name=event_name,
                    date=event_date
                )

                return redirect('admin_dashboard')

        elif action == 'edit':
            event_id = request.POST.get('event_id')
            username = request.POST.get('username')
            password = request.POST.get('password')
            event_name = request.POST.get('event_name')
            event_date = request.POST.get('event_date')

            event = get_object_or_404(Event, id=event_id)

            if Event.objects.filter(date=event_date).exclude(id=event.id).exists():
                error = "Odabrani datum je već zauzet."
            elif User.objects.filter(username=username).exclude(id=event.user.id).exists():
                error = "Korisničko ime već postoji."
            else:
                user = event.user
                user.username = username

                if password:
                    user.set_password(password)

                user.save()

                event.name = event_name
                event.date = event_date
                event.save()

                return redirect('admin_dashboard')

        elif action == 'delete':
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, id=event_id)

            user = event.user
            event.delete()
            user.delete()

            return redirect('admin_dashboard')

    query = request.GET.get('q', '')
    events = Event.objects.all()

    if query:
        events = events.filter(
            Q(name__icontains=query) |
            Q(date__icontains=query)
        )

    return render(request, 'admin_dashboard.html', {
        'events': events,
        'query': query,
        'error': error
    })

@login_required
def seating_plan(request):
    event = Event.objects.get(user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete_guest':
            guest_id = request.POST.get('guest_id')
            Guest.objects.filter(id=guest_id, event=event).delete()

        else:
            full_name = request.POST.get('full_name', '').strip()

            if full_name:
                exists = Guest.objects.filter(
                    event=event,
                    full_name__iexact=full_name
                ).exists()

                if not exists:
                    Guest.objects.create(
                        event=event,
                        full_name=full_name
                    )

        return redirect('seating_plan')

    guests = Guest.objects.filter(event=event)

    return render(request, 'seating_plan.html', {
        'event': event,
        'guests': guests,
    })