from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from newentry.models import Prediction,SensorData
import json

# Create your views here.
def index(request):
    params = request.GET
    
    data = {}

    #get latest temps
    latest_temp = SensorData.objects.latest('time_recorded')
    data['latest_temp'] = latest_temp.temperature

    #get latest prediction
    prediction = Prediction.objects.latest('id')
    data['prediction'] = json.loads(prediction.text_json.replace("'",'"'))
    
    return JsonResponse(data)
