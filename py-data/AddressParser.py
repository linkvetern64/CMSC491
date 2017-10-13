from geopy.geocoders import Nominatim

#
#@param - address - Address to be parsed into Geographical Coordinates
#
def GeoCoords(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    if(location != None):
        print(location.address)
        print(location.latitude, location.longitude)

    else:
        print("Not a valid address, try again...")