# This class provides a sample usage of the GeoCoder.find_place method and the
# PlaceInformation and GeoLocation classes.  It prompts the user for two
# locations and reports the distance between them.

from geolocator import *

def main():
    print("This program finds the distance between two")
    print("places using Google Maps data.")
    print()
    first = input("first location? ")
    one = GeoLocator.find_place(first)
    if (one == None):
        print("no matches for that search string.")
    else:
        print("found at " + str(one))
        second = input("second location? ")
        two = GeoLocator.find_place(second)
        if (two == None):
            print("no matches for that search string.")
        else:
            print("found at " + str(two))
            print(str(one.distance_from(two.get_location())) + " miles apart")
            show_match(1, one)
            show_match(2, two)

# displays information about the passed in place(info)
# labeling it as the number passed in
def show_match(number, info):
    print()
    print("Place # " + str(number))
    print("    name    : " + info.get_name())
    print("    address : " + info.get_address())
    print("    tags    : " + info.get_tag())
    print("    location: " + str(info.get_location()))

main()
