#!/usr/bin/env python

from django.shortcuts import render
from django.views.generic import TemplateView
import os
import sys
import requests
import urllib
import urllib2
import StringIO
from lxml import etree, html

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lake_levels.settings")
import django

django.setup()

from main.models import Lake 


water_api = requests.get('http://www.utah.gov/masterindex/search.json?typeIds=103&limit=50')

response_water = water_api.json()

lakes = []

for result in response_water['results']:

    res = urllib.urlopen(result['url']) 
    html = res.read()

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO.StringIO(html), parser)
    if result['url'] == 'http://stateparks.utah.gov/parks/antelope-island':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
       
        # _xpath = '//*[@id="conditions-widget-2"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)

        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/bear-lake':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-3"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/deer-creek':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-7"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/escalante-petrified-forest':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-10"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/great-salt-lake':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-16"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/gunlock':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-18"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/hyrum':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-45"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/jordanelle':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-23"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/otter-creek':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-26"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/palisade':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-27"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/piute':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-28"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/quail-creek':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-29"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/red-fleet':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-30"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/rockport':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-31"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/sand-hollow':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-32"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/starvation':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-35"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/steinaker':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-36"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/utah-lake':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-40"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    elif result['url'] == 'http://stateparks.utah.gov/parks/yuba':
        new_lake, created = Lake.objects.get_or_create(name=result['name'])
        new_lake.url = result['url']
        new_lake.latitude = result['location']['latitude']
        new_lake.longitude = result['location']['longitude']
        # _xpath = '//*[@id="conditions-widget-43"]/div[2]/div[1]/text()'  
        # filtered_html = tree.xpath(_xpath)
        # filtered_html = "\n".join(filtered_html)
        # print filtered_html

    try: 
        new_lake.save()
    except:
        pass


