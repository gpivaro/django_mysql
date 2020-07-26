from django.shortcuts import render
from .models import TempHumMeas
from django.views.generic import ListView


# Create your views here.
def index(request):
    context = {"posts": TempHumMeas.objects.order_by("-time")[:5]}
    return render(request, "temperaturemonitor/home.html", context)


# Views to plot temperature and humidity meas and pass to Chart.js
def charts(request):
    labels = []
    data1 = data2 = data3 = []
    label1 = ["Sensor 1"]
    label2 = ["Sensor 2"]
    label3 = ["Sensor 3"]
    measurments = TempHumMeas.objects.order_by("-time")[:288]
    for meas in measurments:
        data1.append(meas.temp_sensor_1)
        data2.append(meas.temp_sensor_2)
        labels.append(str(meas.time))

    data_new = data1[0]
    return render(
        request,
        "temperaturemonitor/charts.html",
        {
            "labels": labels,
            "data1": data1,
            "data2": data2,
            "label1": label1,
            "data_new": data_new,
        },
    )

