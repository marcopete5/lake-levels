from django.shortcuts import render
from django.views.generic import TemplateView
import os
import sys
import requests
import urllib
import urllib2
import StringIO
from lxml import etree, html
from main.models import Lake 


class HomeTemplate(TemplateView):
	template_name = 'all_lakes.html'
	
	
def current(request, slug):
	
	context = {}
	

	# this is to get the water conditions

	conditions = Lake.objects.get(slug=slug)
	

	lakes = []

	

	res = urllib.urlopen(conditions.url) 
	html = res.read()

	parser = etree.HTMLParser()
	tree = etree.parse(StringIO.StringIO(html), parser)
	_xpath = '//*[@class="widget parkConditions"]/div[2]/div[1]/text()'  
	_xpaths = '//*[@class="widget parkConditions"]/div[2]/div[2]/text()'
	_xpathss = '//*[@class="widget parkConditions"]/div[2]/div[3]/text()'
	filtered_html = tree.xpath(_xpath)
	filtered_html = tree.xpath(_xpath)
	filtered_html = "\n".join(filtered_html)
	filtered_htmls = tree.xpath(_xpaths)
	filtered_htmls = "\n".join(filtered_htmls)
	filtered_htmlss = tree.xpath(_xpathss)
	filtered_htmlss = "\n".join(filtered_htmlss)
	print filtered_htmlss

	water_temp = filtered_html
	context['water_temp'] = water_temp

	water_level = filtered_htmls
	context['water_level'] = water_level

	ice = filtered_htmlss
	context['ice'] = ice
	# this is to get the current air conditions
	

	latitude = conditions.latitude

	longitude = conditions.longitude

	weather_api = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&units=imperial&appid=ae8f99aabc7314a0f19bdbe90779fdb3' % (latitude, longitude)) 

	response_weather = weather_api.json()
	current_temp = response_weather['main']['temp']
	context['current_temp'] = current_temp
	max_temp = response_weather['main']['temp_max']
	context['max_temp'] = max_temp
	min_temp = response_weather['main']['temp_min']
	context['min_temp'] = min_temp
	wind = response_weather['wind']['speed']
	context['wind'] = wind
	weather = response_weather['weather'][0]['description']
	context['weather'] = weather


	return render(request, 'base.html', context)



