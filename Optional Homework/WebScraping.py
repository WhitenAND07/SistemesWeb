#!/usr/bin/env python
# -*- coding utf-8 -*-

# vim:set fileencoding=utf8

'''

Client Web for https://www.packtpub.com/packt/offers/free-learning/

@Author: JordiBlancoLopez --> 20998

'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):
    def get_web(self, page):
        """Download the web site"""
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        """Search the Title"""
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", "dotd-title")
        title = elements.find("h2")

        if title:
            title = title.text
        else:
            title = "Untitled"

        return title

    def printResult(self, result):
        result = result.replace("\t" ,"")
        result = result.replace("\n", "")

        return result

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/'\
                           'free-learning/')
        result = self.search_text(web)
        result = self.printResult(result)

        # Print Result
        print "The book of PacktPub Today is:"
        print chr(27) + "[1;34m" + result

if __name__ == "__main__":
    client = Client()
    client.main()
