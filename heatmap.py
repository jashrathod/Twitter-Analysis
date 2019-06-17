
import matplotlib.pyplot as plt


# new_york_coordinates = (40.75, -74.00)
# m = gmaps.figure(center=new_york_coordinates, zoom_level=12)
# gmaps.display(m)



# import gmplot
#
# # GoogleMapPlotter return Map object
# # Pass the center latitude and
# # center longitude
# # gmap1 = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 13)
#
# # Pass the absolute path
# # gmap1.draw("map_coordinates.html")
#
# # from_geocode method return the
# # latitude and longitude of given location .
#
# gmaps = googlemaps.Client(key='')
# geocode_result = gmaps.geocode('100 Broadway Street, Missoula, MT')
#
# geom = geocode_result[0]['geometry']
# loc = geom['location']
# lat = loc['lat']
# lng = loc['lng']
#
# gmap2 = gmplot.GoogleMapPlotter.from_geocode("Missoula")
#
# gmap2.draw("map_location.html")



import googlemaps, gmplot, webbrowser, os, json

api_key = ''
gmaps = googlemaps.Client(key=api_key)
geocode_result = gmaps.geocode('100 Broadway Street, Missoula, MT')

# #######
# gmap = gmplot.GoogleMapPlotter.from_geocode("Missoula")    # IF THIS LINE IS HERE, IT THROWS THE ERROR
# #######

geom = geocode_result[0]['geometry']
loc = geom['location']
lat = loc['lat']
lng = loc['lng']

#######
gmap = gmplot.GoogleMapPlotter.from_geocode("Missoula")    # IF THIS LINE IS HERE, IT WORKS
#######

hidden_gem_lat, hidden_gem_lon = lat,lng
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("map_missoula.html")

filename = 'file:///'+os.getcwd()+'/' + 'map_missoula.html'
webbrowser.open_new_tab(filename)


def from_geocode(cls, location_string, api_key, zoom=13):
    lat, lng = cls.geocode(location_string, api_key)
    return cls(lat, lng, zoom, api_key)


# def geocode(self, location_string, api_key):
#     geo_code = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address="%s"&key=%s' % (location_string, api_key))
#     geo_code = json.loads(geo_code.text)
#     latlng_dict = geo_code['results'][0]['geometry']['location']
#     return latlng_dict['lat'], latlng_dict['lng']
