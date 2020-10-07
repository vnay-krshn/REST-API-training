from django.conf.urls import url
from django.urls import path
from countries import views

urlpatterns = [
  url(r'^api/countries$', views.countriesList),
  url(r'^api/countries/(?P<pk>[0-9]+)$', views.countriesDetails)
]

'''
url(r'^api/countries$')
url(r'^api/countries/(?P<pk>[0-9]+)$')
'''