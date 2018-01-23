import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from restaurants.models import RestaurantLocation


def restaurant_listview(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)
