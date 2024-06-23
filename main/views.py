import pytz
from django.shortcuts import render
from .models import Cities, Airports, Airplanes, Bookings, Flights, Gender, Passengers, Routes, Users
# Create your views here.
from django.shortcuts import render
from .forms import SearchFlightsForm


def search_flights(request):
    form = SearchFlightsForm()
    flights = None
    cities = Cities.objects.all()

    if request.method == 'POST':
        form = SearchFlightsForm(request.POST)
        if form.is_valid():
            from_city = form.cleaned_data['from_city']
            to_city = form.cleaned_data['to_city']
            depart_date = form.cleaned_data['depart_date']
            passengers = form.cleaned_data['passengers']

            flights = Flights.objects.filter(
                routeid__startairportid__cityid=from_city,
                routeid__destinationairportid__cityid=to_city,
                departure__date=depart_date
            ).select_related('routeid__startairportid', 'routeid__destinationairportid')

    context = {
        'form': form,
        'flights': flights,
        'cities': cities,
    }
    return render(request, 'main/search_flights.html', context)



def index(request):

    cities = Cities.objects.all()
    airports = Airports.objects.all()
    airplanes = Airplanes.objects.all()
    bookings = Bookings.objects.all()
    flights = Flights.objects.all()
    genders = Gender.objects.all()
    passengers = Passengers.objects.all()
    routes = Routes.objects.all()
    users = Users.objects.all()

    context = {
        'cities': cities,
        'airports': airports,
        'airplanes': airplanes,
        'bookings': bookings,
        'flights': flights,
        'genders': genders,
        'passengers': passengers,
        'routes': routes,
        'users': users,
    }

    return render(request, 'main/index.html',context)