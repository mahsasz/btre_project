from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices



# Create your views here.


def index(request):
    # return HttpResponse('<h1>Hello World</h1>')
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get VMT(Seller of the mounth)
    vmt_realtors = Realtor.objects.all().filter(is_vmt=True)

    context = {
        'realtors' : realtors,
        'vmt_realtors' : vmt_realtors
    }

    return render(request, 'pages/about.html', context)