from django.shortcuts import render
from django.http.response import JsonResponse  # HttpResponse subclass that helps create a JSON encoded response
from rest_framework.parsers import JSONParser  # parser class from rest framework used to accept JSON request
from rest_framework import status  # named const from rest framework used to show http response status code from server after a client request

from countries.models import Countries
from countries.serializer import CountriesSerializer
from rest_framework.decorators import api_view # api wrapper from rest framework used to work with function based views
                                               # helps recieve request instances inside views
# Create your views here.

@api_view(['GET','POST'])
def countriesList(request):
    if request.method == 'GET':
        countries = Countries.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name_icontains = name)

        countriesSerial = CountriesSerializer(countries, many = True)
        return JsonResponse(countriesSerial.data, safe = False)

    elif request.method == 'POST':
        countriesData = JSONParser().parse(request)
        print(countriesData)
        countriesSerial = CountriesSerializer(data = countriesData)
        if countriesSerial.is_valid():
            countriesSerial.save()
            return JsonResponse(countriesSerial.data, status = status.HTTP_201_CREATED)
        return JsonResponse(countriesSerial.errors, status = status.HTTP_404_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])

def countriesDetails(request, pk):
    try:
        countries = Countries.objects.get(pk = pk)
    except Countries.DoesNotExist:
        return JsonResponse({
            'message': 'Country does not exist'
        }, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        countriesSerial = CountriesSerializer(countries)
        return JsonResponse(countriesSerial.data)
    
    elif request.method == 'PUT':
        countriesData = JSONParser().parse(request)
        countriesSerial = CountriesSerializer(countries, data = contriesData)
        if contriesSerial.is_valid():
            contriesSerial.save()
            return JsonResponse(countriesSerial.data)
        return JsonResponse(countriesSerial.errors, status = status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({
            'message': 'Country deleted successfully'
        }, status = status.HTTP_400_BAD_REQUEST)
