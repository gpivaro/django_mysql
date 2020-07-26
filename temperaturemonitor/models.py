from django.db import models


class TempHumMeas(models.Model):
    time = models.DateTimeField()
    temp_sensor_1 = models.FloatField(null=True)
    hum_sensor_1 = models.FloatField(null=True)
    temp_sensor_2 = models.FloatField(null=True)
    hum_sensor_2 = models.FloatField(null=True)
    temp_sensor_3 = models.FloatField(null=True)
    hum_sensor_3 = models.FloatField(null=True)

    def __float__(self):
        return self.temp_sensor_1


# from temperaturemonitor.models import TempHumMeas
# TempHumMeas.objects.all()

