from django.shortcuts import render, redirect
from .forms import PassengerRegistrationForm
from .models import Flights, Passengers
# Create your views here.




def register_passenger(request):
    if request.method == 'POST':
        form = PassengerRegistrationForm(request.POST)
        flight_id = request.POST.get('flight_id')
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.flightid = Flights.objects.get(pk=flight_id)
            passenger.save()
            return redirect('home')  # Перенаправить на страницу успеха после регистрации
    else:
        form = PassengerRegistrationForm()
        flight_id = request.GET.get('flight_id')
    return render(request, 'registration/registration.html', {'form': form, 'flight_id': flight_id})

