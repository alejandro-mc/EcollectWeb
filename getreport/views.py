from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    params = request.GET
    data = {'temp': params['temp'],
            'hum':params['hum'],
            'press':params['press'],
            'srad':params['srad']
           }
    return JsonResponse(data)
