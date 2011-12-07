from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import *

GMAP = GoogleMap(key='AIzaSyD0i-kg-IyNHNMF4Oa_yUjVLvFiOUzmvtg')

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

class FoodLocationMapAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

class FoodLocationAdmin(admin.ModelAdmin):
    pass

class TravelLocationAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Waypoint, admin.GeoModelAdmin)
admin.site.register(Waypoint, GoogleAdmin)
admin.site.register(FoodLocation, FoodLocationAdmin)
admin.site.register(TravelLocation, TravelLocationAdmin)
