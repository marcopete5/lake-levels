from django.shortcuts import render
from django.views.generic import TemplateView
import os
import sys
import requests
import urllib
import urllib2
import StringIO
from lxml import etree, html
from django.core import serializers
from django.http import HttpResponse
from itertools import chain

from main.models import Lake 


class HomeTemplate(TemplateView):
	template_name = 'all_lakes.html'
	
	
# def current(request, slug):
	
# 	context = {}
	

# 	# this is to get the water conditions

# 	conditions = Lake.objects.get(slug=slug)
	

# 	lakes = []

	

# 	res = urllib.urlopen(conditions.url) 
# 	html = res.read()

# 	parser = etree.HTMLParser()
# 	tree = etree.parse(StringIO.StringIO(html), parser)
# 	_xpath = '//*[@class="widget parkConditions"]/div[2]/div[1]/text()'  
# 	_xpaths = '//*[@class="widget parkConditions"]/div[2]/div[2]/text()'
# 	_xpathss = '//*[@class="widget parkConditions"]/div[2]/div[3]/text()'
# 	filtered_html = tree.xpath(_xpath)
# 	filtered_html = tree.xpath(_xpath)
# 	filtered_html = "\n".join(filtered_html)
# 	filtered_htmls = tree.xpath(_xpaths)
# 	filtered_htmls = "\n".join(filtered_htmls)
# 	filtered_htmlss = tree.xpath(_xpathss)
# 	filtered_htmlss = "\n".join(filtered_htmlss)
# 	print filtered_htmlss

# 	water_temp = filtered_html
# 	context['water_temp'] = water_temp

# 	water_level = filtered_htmls
# 	context['water_level'] = water_level

# 	ice = filtered_htmlss
# 	context['ice'] = ice
# 	# this is to get the current air conditions
	

# 	latitude = conditions.latitude

# 	longitude = conditions.longitude

# 	weather_api = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&units=imperial&appid=ae8f99aabc7314a0f19bdbe90779fdb3' % (latitude, longitude)) 

# 	response_weather = weather_api.json()
# 	current_temp = response_weather['main']['temp']
# 	context['current_temp'] = current_temp
# 	max_temp = response_weather['main']['temp_max']
# 	context['max_temp'] = max_temp
# 	min_temp = response_weather['main']['temp_min']
# 	context['min_temp'] = min_temp
# 	wind = response_weather['wind']['speed']
# 	context['wind'] = wind
# 	weather = response_weather['weather'][0]['description']
# 	context['weather'] = weather

# 	image = conditions.image

# 	context['image'] = image


# 	return render(request, 'base.html', context)

def lake_API_view(request):
	request.method == 'POST'

	all_lakes = Lake.objects.all()


	context = {}
	

	
	url = []
	latitudes = []
	longitudes = []
	water_temp = []
	water_level = []
	ice = []
	temp = []
	temperature = []
	max_temperature = []
	min_temperature = []
	wind_speed = []
	weather_conditions = []
	image_list = []

	context['all_lakes'] = []

	for lake in all_lakes:
		temp_dict = {}
		temp = lake.url
		url.append(temp)
		lat = lake.latitude
		latitudes.append(lat)
		lon = lake.longitude
		longitudes.append(lon)


		res = urllib.urlopen(temp) 
		html = res.read()

		parser = etree.HTMLParser()
		tree = etree.parse(StringIO.StringIO(html), parser)
		_xpath = '//*[@class="widget parkConditions"]/div[2]/div[1]/text()'  
		_xpaths = '//*[@class="widget parkConditions"]/div[2]/div[2]/text()'
		_xpathss = '//*[@class="widget parkConditions"]/div[2]/div[3]/text()'
		filtered_html = tree.xpath(_xpath)
		temp_dict['water_temp'] = "\n".join(filtered_html)
		# water_temp.append(filtered_html)
		filtered_htmls = tree.xpath(_xpaths)
		# filtered_htmls 
		temp_dict['water_level'] = "\n".join(filtered_htmls)
		# water_level.append(filtered_htmls)
		filtered_htmlss = tree.xpath(_xpathss)
		temp_dict['ice'] = "\n".join(filtered_htmlss)
		# ice.append(filtered_htmlss)
		


		weather_api = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&units=imperial&appid=ae8f99aabc7314a0f19bdbe90779fdb3' % (lat, lon)) 

		response_weather = weather_api.json()
		
		temp_dict['current_temp'] = response_weather['main']['temp']
		temp_dict['max_temp']= response_weather['main']['temp_max']
		# max_temp = 
		temp_dict['min_temp'] = response_weather['main']['temp_min']
		# min_temp = 
		# min_temperature.append(min_temp)
		temp_dict['wind'] = response_weather['wind']['speed']
		# wind = 
		# wind_speed.append(wind)
		temp_dict['weather'] = response_weather['weather'][0]['description']
		# weather = 
		# weather_conditions.append(weather)
		temp_dict['image'] = lake.image
		# image = 
		# image_list.append(image)
		temp_dict['name'] = lake.name 
		temp_dict['slug'] = lake.slug
		context['all_lakes'].append(temp_dict)
	
	print context['all_lakes']



    # context = {all_lakes:[{w:5,c:5},{w:3,c:90},{w:1,c:10}]}
	# url = dict(zip('url', url))
	# latitudes = dict(zip('latitudes', latitudes))
	# longitudes = dict(zip('longitudes', longitudes))
	# water_temp = dict(zip('water_temp', water_temp))
	# water_level = dict(zip('water_level', water_level))
	# ice = dict(zip('ice', ice))
	# temp = dict(zip('temp', temp))
	# temperature = dict(zip('temperature', temperature))
	# max_temperature = dict(zip())
	# min_temperature = dict(zip())
	# wind_speed = dict(zip())
	# weather_conditions = dict(zip())
	# image_list = dict(zip())


	# name_values = dict(zip())		
	# zipper = dict(zip(all_lakes.name,????)) 
	# 	url, latitudes, longitudes, water_temp, water_level, ice, temp, temperature, max_temperature, min_temperature, wind_speed, weather_conditions, image_list))
	

	# context['image'] = image_list
	# context['water_temp'] = water_temp
	# context['water_level'] = water_level
	# context['ice'] = ice
	# context['current_temp'] = temperature
	# context['max_temp'] = max_temperature
	# context['min_temp'] = min_temperature
	# context['wind'] = wind_speed
	# context['weather'] = weather_conditions
	# context['all_lakes'] = all_lakes

	return render(request, 'base.html', context)








