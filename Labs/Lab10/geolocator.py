# This class provides a single static method called find that provides access
# to the Google Maps api.  It takes a search string and returns the latitude
# and longitude of the top hit for the search.  Returns null if the search
# produces no results or if no internet connection is available.
#
# Sample calls:
#     location = GeoLocator.find("space needle")
#     location = GeoLocator.find_place("space needle")

import urllib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as et

from place_information import *
from geolocation import *

class GeoLocator:    
    # Given a query string, returns a GeoLocation representing the coordinates
    # of Google's best guess at what the query string represents.
    #
    # Returns None if there are no results for the given query, or if we
    # cannot connect to the Maps API.
    @staticmethod
    def find(location):
        root = GeoLocator.__get_xml(location)
        if(root == None):
            return None

        result = root.find('result').find('geometry').find('location')    
        lat = float(result.find('lat').text)
        lng = float(result.find('lat').text)
        return GeoLocation(lat, lng)

    # Given a query string, returns a PlaceInformation representing the data
    # of Google's best guess at what the query string represents.
    #
    # Returns None if there are no results for the given query, or if we
    # cannot connect to the Maps API.
    @staticmethod
    def find_place(location):
        root = GeoLocator.__get_xml(location)
        if(root == None):
            return None

        result = root.find('result').find('geometry').find('location')
        lat = float(result.find('lat').text)
        lng = float(result.find('lat').text)
        address = root.find('result').find('formatted_address').text
        name = root.find('result').find('address_component').find('long_name').text
        #tag = " ".join(root.find('result').findall('type'))
        tag = root.find('result').find('type').text
        return PlaceInformation(name, address, tag, lat, lng)


    # takes a location string to search the Google Maps API for as a parameter
    # returns an XML object with data about the search
    @staticmethod
    def __get_xml(location):    
        url_string = ("https://maps.googleapis.com/maps/api/geocode/xml?sensor=false&address=" +
                      urllib.parse.quote_plus(location))
        try:
            # Get the first result in the XML document, bail if no results
            f = urllib.request.urlopen(url_string)
            xml = f.read()
            root = et.fromstring(xml)
            result = root.find('result').find('geometry').find('location')
            
            if (None == result or "" == result):
                # No results found for query.
                return None
            
            return root
        except RuntimeError:
            print(Error)
        
        # Given any failures trying to retrieve results...
        return None

