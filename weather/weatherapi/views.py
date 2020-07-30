from django.shortcuts import render
import requests
from django.http import HttpResponse
from weatherapi.key import api_key
# Create your views here.
def indexView(request):
    return render(request, "weatherapi/index.html")

def resultView(request):
    if request.method == "POST":
        city_name = request.POST["city"]
        if city_name == "":
            return render(request , "weatherapi/index.html")
        else:
            city_name = city_name.lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        weather_data = requests.get(url).json()
        print(weather_data)
        try:
            context = {
                ####
                "city_name":weather_data["city"]["name"],
                "city_country":weather_data["city"]["country"],
                "city_population":weather_data["city"]["population"],
                ####
                "temp": round(weather_data["list"][0]["main"]["temp"] -273.0),
                "temp_min":round(weather_data["list"][0]["main"]["temp_min"] -273.0),
                "temp_max": round(weather_data["list"][0]["main"]["temp_max"] -273.0),
                ###
                "pressure":weather_data["list"][0]["main"]["pressure"],
                "humidity":weather_data["list"][0]["main"]["humidity"],
                "sea_level":weather_data["list"][0]["main"]["sea_level"],

                ####
                "weather":weather_data["list"][1]["weather"][0]["main"],
                "description":weather_data["list"][1]["weather"][0]["description"],
                "icon":weather_data["list"][1]["weather"][0]["icon"],
            }
        except:
            context = {
            ####
            "city_name":"Try Again With Other City",
            "city_country":"Try Again With Other City",
            "city_population":"Try Again With Other City",
            ####
            "temp": "Try Again With Other City",
            "temp_min":"Try Again With Other City",
            "temp_max":"Try Again With Other City",
            ###
            "pressure":"Try Again With Other City",
            "humidity":"Try Again With Other City",
            "sea_level":"Try Again With Other City",

            ####
            "weather":"Try Again With Other City",
            "description":"Try Again With Other City",
            "icon":"Try Again With Other City",

            }


        return render(request, "weatherapi/result.html", context)

    else:
        return render(request , "weatherapi/index.html")
        # return HttpResponse(context)
