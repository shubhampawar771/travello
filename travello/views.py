from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'mumbai'
    dest1.desc = 'City never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 790
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'Capital City'
    dest2.img = 'destination_2.jpg'
    dest2.price = '1200'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.desc = 'Historical City'
    dest3.img = 'destination_3.jpg'
    dest3.price = '1000'
    dest3.offer = True

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})