from django.contrib.gis.db import models
from geopy import geocoders

class Waypoint(models.Model):
    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)

class FoodLocation(models.Model):
    title_slug = models.SlugField(unique=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    original_address = models.TextField()
    place = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zipcode =models.CharField(max_length=10, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    geometry = models.PointField(blank=True, null=True)
    #date published

    def __unicode__(self):
        #return '%s %s ( %s, %s )' % (self.title_slug, self.place, self.geometry.x, self.geometry.y)
        return '%s %s' % (self.title_slug, self.place)

    def save(self):
        geocoder = geocoders.Google()

        geocoding_results = None
        try:
            geocoding_results = list(geocoder.geocode(self.original_address, exactly_one=True))
        except:
            pass

        if geocoding_results:
            self.place, (self.lat, self.lng) = geocoding_results
            self.geometry = 'POINT(%f %f)' % (self.lat, self.lng)

        super(FoodLocation, self).save()

class TravelLocation(models.Model):
    title_slug = models.SlugField(unique=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    original_address = models.TextField()
    place = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zipcode =models.CharField(max_length=10, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    geometry = models.PointField(blank=True, null=True)
    #date published

    def __unicode__(self):
        #return '%s %s ( %s, %s )' % (self.title_slug, self.place, self.geometry.x, self.geometry.y)
        return '%s %s' % (self.title_slug, self.place)

    def save(self):
        geocoder = geocoders.Google()

        geocoding_results = None
        try:
            geocoding_results = list(geocoder.geocode(self.original_address, exactly_one=True))
        except:
            print "error geopy"

        if geocoding_results:
            self.place, (self.lat, self.lng) = geocoding_results
            self.geometry = 'POINT(%f %f)' % (self.lat, self.lng)

        super(TravelLocation, self).save()