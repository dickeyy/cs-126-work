# Import goelocation class
from geolocation import *

# Define the placeinformation class
class PlaceInformation:
    # Define the constructor
    def __init__(self, name, address, tag, latitude, longitude):
        self.__name = name
        self.__address = address
        self.__tag = tag
        self.__location = GeoLocation(latitude, longitude)

    # Define the main functions
    # define the get_name function returns the name set in the constructor
    def get_name(self):
        return self.__name

    # define the get_address function returns the address set in the constructor
    def get_address(self):
        return self.__address

    # define the get_tag function returns the tag set in the constructor
    def get_tag(self):
        return self.__tag

    # Define the __str__ function to return the name, address, and tag
    def __str__(self):
        return self.__name + " (" + str(self.__location) + ")"

    # define the get_location function returns the location set in the constructor
    def get_location(self):
        return self.__location

    # define the distance_from function returns the distance from the location set in the constructor
    def distance_from(self, spot):
        return self.__location.distance_from(spot)