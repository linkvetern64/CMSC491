from geopy.geocoders import Nominatim
from smartystreets import Client
#
#@param - address - Address to be parsed into Geographical Coordinates
#@param - timeout - Time in seconds until Exception is thrown, set to None if you want no timeout
#
def GeoCoords(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address, True, timeout=10)

    if(location != None):
        print(location.address)
        print(location.latitude, location.longitude)

    else:
        print("Not a valid address, try again...")


def GeoCoordsSmarty(address):
    print(address)