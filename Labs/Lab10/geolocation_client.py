# Impor the geolocation class
from geolocation import *

def main():
    get_place_info()

def get_place_info():
    # Print the intro
    print("the stash is at latitude: 34.988889, longitude: -106.614444")
    print("ABQ studio is at latitude: 34.989978, longitude: -106.614357")
    print("FBI building is at latitude: 35.131281, longitude: -106.61263")
    print("Distance in miles between:")

    # Use the geolocation class to store the lat and long of the stash
    stash = GeoLocation(34.988889, -106.614444)
    # Use the geolocation class to store the lat and long of the ABQ studio
    abq = GeoLocation(34.989978, -106.614357)
    # Use the geolocation class to store the lat and long of the FBI building
    fbi = GeoLocation(35.131281, -106.61263)

    # Use the geolocation class to calculate the distance between the stash and the ABQ studio
    stash_abq = stash.distance_from(abq)
    # Use the geolocation class to calculate the distance between the stash and the FBI building
    stash_fbi = stash.distance_from(fbi)
    # Use the geolocation class to calculate the distance between the ABQ studio and the FBI building
    abq_fbi = abq.distance_from(fbi)

    # Print the distance between the stash and the ABQ studio
    print("stash and ABQ studio: ", stash_abq)
    # Print the distance between the stash and the FBI building
    print("stash and FBI building: ", stash_fbi)
    # Print the distance between the ABQ studio and the FBI building
    print("ABQ studio and FBI building: ", abq_fbi)

main()
