from django.conf.urls.defaults import *

urlpatterns = patterns('geofood.maps.views',
    url(r'^$', 'index', name='maps-index'),
)
