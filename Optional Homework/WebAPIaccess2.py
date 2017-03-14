#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim : set fileenconding=utf8 :

'''
Client Web per http://api.wunderground.com/api/******************/satellite/q/CA/Spain/Lleida.xml
               http://api.wunderground.com/api/******************/astronomy/q/Lleida.xml

@Author: JordiBlancoLopez --> 20998
'''

import sys
import urllib2
from bs4 import BeautifulSoup


api_key = None

class WeatherClient(object):
    """docsstring for WeatherClient"""
    url_base = "http://api.wunderground.com/api/"
    url_service = {
        "astronomy": "/astronomy/q/",
        "satellite": "/satellite/q/CA/"
    }
    format = ".xml"

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def get_web(self, location, url_service):
        # Download the web

        url = WeatherClient.url_base + self.api_key + \
              url_service + location + WeatherClient.format

        f = urllib2.urlopen(url)
        data = f.read()
        f.close()

        return data

    def astronomy (self, location):
        """Read the site hourly"""
        data = self.get_web(location, WeatherClient.url_service["astronomy"])

        soup = BeautifulSoup(data, 'lxml')
        moon_phase = soup.find("moon_phase")

        percentIlluminated = moon_phase.find("percentilluminated").text
        ageOfMoon = moon_phase.find("ageofmoon").text
        sunseth = moon_phase.find("sunset").find("hour").text
        sunsetm = moon_phase.find("sunset").find("minute").text

        sunriseh = moon_phase.find("sunrise").find("hour").text
        sunrisem = moon_phase.find("sunrise").find("minute").text
        moonseth = moon_phase.find("moonset").find("hour").text
        moonsetm = moon_phase.find("moonset").find("minute").text

        moonriseh = moon_phase.find("moonrise").find("hour").text
        moonrisem = moon_phase.find("moonrise").find("minute").text

        sun_phase = soup.find("sun_phase")

        sunseth_s = sun_phase.find("sunset").find("hour").text
        sunsetm_s = sun_phase.find("sunset").find("minute").text
        sunriseh_s = sun_phase.find("sunrise").find("hour").text
        sunrisem_s = sun_phase.find("sunrise").find("minute").text

        resultats = {}
        resultats["moon_phase"] = {}
        resultats["sun_phase"] = {}

        resultats["moon_phase"] ["percentIlluminated"] = percentIlluminated
        resultats["moon_phase"]["ageOfMoon"] = ageOfMoon
        resultats ["moon_phase"] ["sunset"] = sunseth + ":" + sunsetm +"h"

        resultats["moon_phase"]["sunrise"] = sunriseh + ":" + sunrisem + "h"
        resultats["moon_phase"]["moonset"] = moonseth + ":" + moonsetm + "h"
        resultats["moon_phase"]["moonrise"] = moonriseh + ":" + moonrisem + "h"

        resultats["sun_phase"]["sunset"] = sunseth_s + ":" + sunsetm_s + "h"
        resultats["sun_phase"]["sunrise"] = sunriseh_s + ":" + sunrisem_s + "h"

        # Return the result
        return resultats

    def satellite(self, location):
        """Read the site hourly"""
        data = self.get_web(location, WeatherClient.url_service["satellite"])

        soup = BeautifulSoup(data, 'lxml')
        satellite = soup.find("satellite")

        image_url = satellite.find("image_url").text
        image_url_ir4 = satellite.find("image_url_ir4").text
        image_url_vis = satellite.find("image_url_vis").text


        resultats = {}
        resultats["satellite"] = {}

        resultats["satellite"]["image_url"] = image_url
        resultats["satellite"]["image_url_ir4"] = image_url_ir4
        resultats["satellite"]["image_url_vis"] = image_url_vis

        # Return the result
        return resultats

if __name__ == "__main__" :

    location = "Lleida"
    location_astronomy = "Spain/"+ location

    if not api_key:
        try:
            api_key = sys.argv[1]
            wc = WeatherClient(api_key)

            resultAstronomy = wc.astronomy(location_astronomy)
            resultSatellite = wc.satellite(location)

            print "Astronomy about " + location_astronomy + ":\n"
            print resultAstronomy

            print "\n"

            print "Satellite about " + location + ":\n"
            print resultSatellite

        except IndexError:
            print "API Key must be in CLI option"