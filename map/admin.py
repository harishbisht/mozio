from django.contrib import admin
from .models import Map, Location
# Register your models here.


class LocationInline(admin.StackedInline):
    model = Location
    extra = 6


class MapAdmin(admin.ModelAdmin):
    inlines = [
        LocationInline,
    ]

admin.site.register(Map,MapAdmin)