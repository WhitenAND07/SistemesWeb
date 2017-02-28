#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim : set fileenconding=utf8 :

'''
Client Web per http://api.wunderground.com/api/******************/almanac/q/CA/Lleida.xml

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
        "almanac" : "almanac/q/CA/"
    }

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def almanac (self, location):
        # Download the web

        url = WeatherClient.url_base + self.api_key + WeatherClient.url_service["almanac"] + \
            location + ".xml"

        f = urllib2.urlopen(url)
        data = f.read()
        f.close()

        #Read the site

        soup = BeautifulSoup(data, 'lxml')
        maximes = soup.find("temp_high")
        normal = maximes.find("normal").find("c").text
        record = maximes.find("record").find("c").text

        minimes = soup.find("temp_low")
        normal_l = minimes.find("normal").find("c").text
        record_l = minimes.find("normal").find("c").text

        resultats = {}
        resultats ["maximes"] = {}
        resultats ["minimes"] = {}
        resultats["maximes"] ["normal"] = normal
        resultats["minimes"]["normal"] = normal_l
        resultats["maximes"]["record"] = record
        resultats["minimes"]["record"] = record_l

        # Return the result
        return resultats

if __name__ == "__main__" :

    if not api_key:
        try:
            api_key = sys.argv[1]

        except IndexError:
            print "API Key must be in CLI option"

    wc = WeatherClient(api_key)
    resultat = wc.almanac("Lleida")
    print resultat

