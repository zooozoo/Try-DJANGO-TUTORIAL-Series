from django.contrib import admin

# Register your models here.
from restaurants.models import RestaurantLocation
#
class TimeRestaurantLocation(admin.ModelAdmin):
    readonly_fields = ('timestamp','updated',)

admin.site.register(RestaurantLocation, TimeRestaurantLocation)