#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim : set fileenconding=utf8 :

'''
Client Web per http://api.wunderground.com/api/******************/hourly/q/CA/Lleida.xml

@Author: JordiBlancoLopez
'''

import sys
import urllib2
from bs4 import BeautifulSoup


api_key = None

class WeatherClient(object):
    """docsstring for WeatherClient"""

    url_base = "http://api.wunderground.com/api/"
    url_service = {
        "hourly" : "/hourly/q/CA/"
    }

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def hourly (self, location):
        # Download the web

        url = WeatherClient.url_base +self.api_key + \
              WeatherClient.url_service["hourly"] + location + ".xml"

        f = urllib2.urlopen(url)
        data = f.read()
        f.close()

        #Read the site
        soup = BeautifulSoup(data, 'lxml')
        forecast = soup.find("forecast")
        hour = forecast.find("FCTTIME").find("pretty").text
        temperature = forecast.find("temp").find("metric").text
        dewpoint = forecast.find("dewpoint").find("metric").text
        wspd = forecast.find("wspd").find("metric").text
        wdir = forecast.find("wdir").find("dir").text
        windchill = forecast.find("windchill").find("metric").text
        heatindex = forecast.find("heatindex").find("metric").text
        feelslike = forecast.find("feelslike").find("metric").text
        qpf = forecast.find("qpf").find("metric").text
        snow = forecast.find("snow").find("metric").text
        mslp = forecast.find("mslp").find("metric").text


        resultats = {}
        resultats ["forecast"] = {}
        resultats["forecast"] ["FCTTIME"] = hour
        resultats["forecast"]["temp"] = temperature
        resultats ["forecast"] ["dewpoint"] = dewpoint
        resultats["forecast"] ["wspd"] = wspd
        resultats["forecast"]["wdir"] = wdir
        resultats["forecast"]["windchill"] = windchill
        resultats["forecast"]["heatindex"] = heatindex
        resultats["forecast"]["feelslike"] = feelslike
        resultats["forecast"]["qpf"] = qpf
        resultats["forecast"]["snow"] = snow
        resultats["forecast"]["mslp"] = mslp
        # Return the result
        return resultats

if __name__ == "__main__" :

    if not api_key:
        try:
            api_key = sys.argv[1]

        except IndexError:
            print "API Key must be in CLI option"

    wc = WeatherClient(api_key)
    resultat = wc.hourly("Lleida")
    print resultat