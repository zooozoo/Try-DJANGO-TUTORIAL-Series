import random

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from restaurants.forms import RestaurantCreateForm
from restaurants.models import RestaurantLocation


def restaurant_createview(request):
    form =RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
            name=form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category')
        )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, template_name, context)


def restaurant_listview(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(catecory__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj
