from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key={APIKEY}&include=minutely')
    posts = response.json()
    data = posts['data']
    for a in data:
        print(a["timezone"])
    return render(request, 'index.html',{"posts":posts})
