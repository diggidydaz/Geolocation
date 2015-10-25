from geolocation.google_maps import GoogleMaps
import IP2Location
import geoip2.database

# Enter GoogleMap API Key
google_maps = GoogleMaps(api_key='AIzaSyDJvXt5YtoHbMkQFBQk-Nok5SgdLwpF5R4')

#Define Address for Lookup
address = "New York City Wall Street 12"
location = google_maps.search(location=address)  # sends search to Google Maps.
my_location = location.first()  # returns only first location.

# Read GeoLite Database for IP Address Lookup
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

#Enter IP Address for Lookup
response = reader.city('208.30.113.22')

#Print IP Address information
print("====================")
print(response.city.name)
print(response.postal.code)
print(response.location.latitude)
print(str(response.location.longitude) + " \n")

#Google Maps IP Coordinate look up
print("My Location - Lat " + str(my_location.lat))
print("My Location - Long " + str(my_location.lng))

# reverse geocode
lat = 40.7060008
lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()
print(str(my_location) + " <---")