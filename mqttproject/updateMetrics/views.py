from django.shortcuts import render
# from threading import Thread
# from .mqtt_python_subscriber import run
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

# Create your views here.
def index(request):
    return render(request, "updateMetrics/index.html")


def section(request, num):
    if (num == 0):
        # temp
        with open("updateMetrics/temperature.txt", 'r') as f:
            ret = os.read(f, 1024).decode()
            return HttpResponse(ret)
    elif (num == 1):
        # hum
        with open("updateMetrics/humidity.txt", 'r') as f:
            ret = os.read(f, 1024).decode()
            return HttpResponse(ret)
    else:
        raise Http404("No such topic")
