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
        "almanac": "/almanac/almanac/q/CA/"
    }

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def get_web(self, location):
        """Download the web"""
        url = self.url_base + self.api_key + self.url_service["almanac"] + \
              location + ".xml"
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
        return data

    def almanac (self, location):
        """Read the site"""
        data = self.get_web(location)

        soup = BeautifulSoup(data, 'lxml')

        result = {}
        result["maximes"] = {}
        result["minimes"] = {}

        maximes = soup.find("temp_high")
        result["maximes"]["normal"] = maximes.find("normal").find("c").text
        result["maximes"]["record"] = maximes.find("record").find("c").text

        minimes = soup.find("temp_low")
        result["minimes"]["normal"] = minimes.find("normal").find("c").text
        result["minimes"]["record"] = minimes.find("record").find("c").text

        # Return the result
        return result

if __name__ == "__main__" :

    if not api_key:
        try:
            api_key =  sys.argv[1]
            wc = WeatherClient(api_key)
            result = wc.almanac("Lleida")
            print result
        except IndexError:
            print "API Key must be in CLI option"
