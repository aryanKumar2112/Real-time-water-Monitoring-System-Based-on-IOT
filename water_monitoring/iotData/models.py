from django.db import models


class IotData(models.Model):
    temperature = models.FloatField()
    pHValue =  models.FloatField()
    turbidity = models.FloatField()