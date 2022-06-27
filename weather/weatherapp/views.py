from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def home(request):
	if request.method=='POST':
		search=request.POST['search']
		api_request=requests.get(f'https://nepal-weather-api.herokuapp.com/api/?place={search}')
	else:
		api_request=requests.get('https://nepal-weather-api.herokuapp.com/api/?placenp=Kathmandu')

	try:
		api=json.loads(api_request.content)
	except exception as e:
		api="sorry ! data not found."
	return render(request, 'weather.html', {'api':api})