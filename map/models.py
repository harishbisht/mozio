from django.db import models
from django.utils.translation import ugettext as _
from provider.models import Provider


class Map(models.Model):
	Dealername= models.ManyToManyField(Provider, blank=True)
	

class Location(models.Model):
	Dealer = models.ForeignKey(Map, related_name='MapLocation')
	Lat = models.FloatField(_('Latitude'), blank=True, null=True)
	Lon = models.FloatField(_('Longitude'), blank=True, null=True)