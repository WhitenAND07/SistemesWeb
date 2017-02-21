#!/usr/bin/env python
#-*- coding utf-8 -*-
#vim:set fileencoding=utf8

'''
Client Web per www.udl.cat

@Author: JordiBlancoLopez
'''
import urllib2
from bs4 import BeautifulSoup

class Client(object):
	def get_web(self, page):
		"""baixar-se la web"""
		f = urllib2.urlopen(page)
		html = f.read()
		f.close()
		return html

	def search_text(self, web):
		"""buscar el text"""
		soup = BeautifilSoup(html, 'html.parser')
		elements = soup.find.all("div", "featured-link")
		for element in elements:
			data = element.find("time")
		return elements

	def main(self):
		web = self.get_web('http://www.udl.cat/')
		resultat = self.search_text(web)

		# imprimir resultats
		print web

if __name__ == "__main__":
	client = Client()
	client.main()
