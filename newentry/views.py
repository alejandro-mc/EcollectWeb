from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from newentry.models import SensorData,Prediction
import dateutil.parser as duparser

# insert sensor data into db.
def insert(request):
    params = request.GET

    #insert entry
    newentry = SensorData()
    newentry.temperature   = float(params['temp'])
    newentry.pressure      = float(params['press'])
    newentry.humidity      = float(params['hum'])
    newentry.time_recorded = duparser.parse(params['datetime'])
    newentry.sensor_id     = int(params['sensorId'])
    try:
       newentry.save()
       return JsonResponse({'status':'succeeded'})
    except:
       return JsonResponse({'status':'failed'})


#insert prediction into db
def insertPrediction(request):
    params = request.GET


    #insert new prediction
    new_prediction = Prediction()
    new_prediction.text_json = params['prediction']
    try:
      new_prediction.save()
    except:
      return JsonResponse({'status':'insertion failed'})    
    

    #delete old prediction
    
    old_prediction = Prediction.objects.earliest('id')
    try:
      old_prediction.delete()    
      return JsonResponse({'status':'succeeded'})    
    except: 
      return JsonResponse({'status':'deletion failed'})    
    
