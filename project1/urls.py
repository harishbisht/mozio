from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from provider import views



urlpatterns = [
    # Examples:
    url(r'^$', 'map.views.home', name='home'),
    url(r'^provider/', views.ProviderList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
