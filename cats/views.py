import requests

from django.shortcuts import render


THECATS_URL = 'https://api.thecatapi.com/v1/images/search'

def home_view(request):
    req = requests.get(THECATS_URL, params={'limit': 3, 'size': 'full'})

    images = req.json()

    context = {'images': images}

    return render(request, 'cats/index.html', context)
