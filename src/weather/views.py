from os import name
from django.shortcuts import redirect, render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages
from .forms import CityForm
from .models import City
# Create your views here.

def index(request):
    form = CityForm()
    cities = City.objects.all()
    url = config("BASE_URL")
    # city ="Berlin"
    # r = requests.get(url.format(city))
    # content=r.json()
    # print(type(a))
    # pprint(a)
    if request.method=="POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city =form.cleaned_data["name"]
            if not City.objects.filter(name= new_city).exists():
                r = requests.get(url.format(new_city))
                if r.status_code ==200:
                    form.save()
                    messages.success(request, "Successfully added..")
                    
                else:
                    messages.warning(request, "There is no city like that. Sure type city correctly..")
                    
            else:
                messages.warning(request, "City has already added..")
            return redirect("home")
    city_data =[]
    for city in cities:
        r = requests.get(url.format(city))
        # print(r.status_code)
        content=r.json()
        
        weather_data ={
            'city':city.name,
            'temp':content["main"]["temp"],
            "description":content["weather"][0]["description"],
            "icon":content["weather"][0]["icon"]
            
            
        }
        city_data.append(weather_data)
        # print(city_data)
        context ={
            'city_data':city_data,
            'form':form,
       }
    return render(request, "weather/index.html", context)
