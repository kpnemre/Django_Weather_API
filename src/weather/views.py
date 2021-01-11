from django.shortcuts import render
from decouple import config
import requests

# Create your views here.

def index(request):
    url = config("BASE_URL")
    city ="Berlin"
    r = requests.get(url.format(city))
    print(r)
    return render(request, "weather/index.html")
