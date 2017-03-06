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
            title = "Sense Titol"

        return title

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        resultat = self.search_text(web)

        # Print Result
        print resultat


if __name__ == "__main__":
    client = Client()
    client.main()
