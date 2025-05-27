from django.shortcuts import render, get_object_or_404, redirect
from .models import SportFacility, Reservation, Pricing, UserProfile
from django.contrib import messages
from .forms import ReservationForm, ReviewForm, ContactForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def index(request):
    facilities = SportFacility.objects.all()
    
    return render(request, 'index.html', {'facilities': facilities})



def facility_detail(request, pk):
    facility = get_object_or_404(SportFacility, pk=pk)
    pricing = Pricing.objects.filter(facility=facility).first()

    return render(request, 'facility_detail.html', {
        'facility': facility,
        'pricing': pricing,
    })  

@login_required
def reservation_list(request):
    facility_id = request.GET.get('facility')
    if facility_id:
        reservations = Reservation.objects.filter(facility_id=facility_id)
    else:
        reservations = Reservation.objects.all()
    return render(request, 'user_reservations.html', {'reservations': reservations})

@login_required
def reservation_create(request, pk):
    facility = get_object_or_404(SportFacility, pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST, facility=facility, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.facility = facility
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Rezervace byla úspěšně vytvořena!')
            return redirect('index')
        else:
            
            messages.error(request, 'V daném termínu již existuje rezervace. Zvolte jiný čas.')
    else:
        form = ReservationForm(facility=facility, user=request.user)

    
    reservations = Reservation.objects.filter(facility=facility).order_by('date', 'start_time')

    return render(request, 'reservation_form.html', {
        'form': form,
        'facility': facility,
        'reservations': reservations,
    })

@login_required
def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation_edit.html', {
        'form': form,
        'reservation': reservation,
    })

@login_required
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if reservation.user != request.user:
        return HttpResponseForbidden("Nemáte oprávnění mazat tuto rezervaci.")

    if request.method == 'POST':
        reservation.delete()
        return redirect('user_reservations')

    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})


@login_required
def facility_reviews(request, pk):
    facility = get_object_or_404(SportFacility, pk=pk)
    reviews = facility.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.facility = facility
            review.save()
            messages.success(request, 'Recenze byla úspěšně přidána.')
            return redirect('facility_reviews', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'facility_reviews.html', {
        'facility': facility,
        'reviews': reviews,
        'form': form,
    })


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Zde můžeš poslat email, uložit zprávu apod.
            messages.success(request, 'Zpráva byla úspěšně odeslána!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrace proběhla úspěšně.')
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Přihlášen jako {username}')
                return redirect('index')
            else:
                messages.error(request, 'Neplatné přihlašovací údaje.')
        else:
            messages.error(request, 'Neplatný formulář.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Byl jsi úspěšně odhlášen.')
    return redirect('index')


@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile.html', {'profile': profile})

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('date', 'start_time')
    return render(request, 'user_reservations.html', {'reservations': reservations})