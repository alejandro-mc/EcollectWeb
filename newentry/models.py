from django.db import models

class WeatherStations(models.Model):
      station_type  = models.PositiveSmallIntegerField()#1- for outside 2- for inside
      name          = models.CharField(max_length = 30,null=False)
      code          = models.CharField(max_length = 30,null=True)
      latitude      = models.DecimalField(max_digits=6,decimal_places=4)
      longitude     = models.DecimalField(max_digits=7,decimal_places=4)

      
class WeatherData(models.Model):
      station         = models.ForeignKey(WeatherStations,on_delete=models.CASCADE)
      time_recorded   = models.DateTimeField(auto_now=False,auto_now_add=False,null=False)
      temperature     = models.DecimalField(max_digits=6,decimal_places=2,null=True)
      pressure       = models.DecimalField(max_digits=6,decimal_places=2,null=True)
      humidity        = models.DecimalField(max_digits=6,decimal_places=2,null=True)
      windspeed       = models.PositiveSmallIntegerField(null=True)
      solar_radiation = models.PositiveSmallIntegerField(null=True)      


class Sensors(models.Model):
      mac       = models.CharField(max_length=17)
      note      = models.CharField(max_length = 200,null=False)
      

class SensorData(models.Model):
      sensor          = models.ForeignKey(Sensors,on_delete=models.PROTECT)
      time_recorded   = models.DateTimeField(auto_now=False,auto_now_add=False,null=False)
      temperature     = models.DecimalField(max_digits=6,decimal_places=2,null=True)
      pressure        = models.DecimalField(max_digits=6,decimal_places=2,null=True)
      humidity        = models.DecimalField(max_digits=6,decimal_places=2,null=True)


class Prediction(models.Model):
      text_json  = models.TextField()
