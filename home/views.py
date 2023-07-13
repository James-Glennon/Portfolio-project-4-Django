from django.shortcuts import render
from bookings.models import Guest, Tables, Booking

# Create your views here.


def index_view(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def bookings_view(request):
    """ A view to return the bookings page """
    guests = Guest.objects.values_list('first_name')
    context = {
        'guests': guests,
    }

    return render(request, 'home/bookings.html', context)
