from django.shortcuts import render_to_response
from django.template import RequestContext
from maps.models import *

def index(request):

    return render_to_response('maps/index.html', {'location': FoodLocation.objects.all(), 'travel': TravelLocation.objects.all()}, context_instance = RequestContext(request))

