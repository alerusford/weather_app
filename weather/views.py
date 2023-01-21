from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    api_key = 'e90ff88039119e31365efe5760a1b750'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name))
        res = res.json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)


    content = {'all_info': all_cities, 'form': form}

    
    return render(request, 'weather/index.html', content)

