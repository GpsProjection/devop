# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:33:13 2015

@author: Administrator
"""

from googlemaps2 import GoogleMaps
api_key="AIzaSyDNl2UKKkyanLn1go_jNAP6r_tPeMf57kA"
gmaps=GoogleMaps(api_key)
reverse=gmaps.reverse_geocode(38.887563,-77.019929)
address=reverse['Placemark'][0]['address']
print (address)