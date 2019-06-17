import pandas as pd
import numpy as np
import googlemaps
import gmaps as gm

API_KEY = ''
gm = googlemaps.Client(key=API_KEY)

data = pd.read_csv('MetroManilaSpatialAccidentData.csv', encoding = "ISO-8859-1", low_memory=False, index_col = 'Key')
data = data.fillna('')                   # fill empty entries with ''
print(list(data))                        # print Variable Name
# data.head()                              # show some data

[maxRow,maxCol]=data.shape
# maxRow,maxCol


def Geocode(query):
    # do geocoding
    try:
        geocode_result = gm.geocode(query)[0]
        latitude = geocode_result['geometry']['location']['lat']
        longitude = geocode_result['geometry']['location']['lng']
        return latitude, longitude
    except IndexError:
        return 0


def GeocodeStreetLocationCity(data):
    lat = []  # initialize latitude list
    lng = []  # initialize longitude list
    start = data.index[0]  # start from the first data
    end = data.index[maxRow - 1]  # end at maximum number of row
    for i in range(start, end + 1, 1):  # iterate all rows in the data
        isSuccess = True  # initial Boolean flag
        query = data.Street[i] + ' ' + data.Location[i] + ' ' + data.City[
            i]  # try set up our query street-location-city
        result = Geocode(query)
        if result == 0:  # if not successful,
            query = data.Location[i] + ' ' + data.City[i]  # try set up another query location-city
            result = Geocode(query)
            if result == 0:  # if still not successful,
                query = data.Street[i] + ' ' + data.City[i]  # try set up another query street-city
                result = Geocode(query)
                if Geocode(query) == 0:  # if still not successful,
                    isSuccess = False  # mark as unsuccessful
                    print(i, 'is failed')
                else:
                    print(i, result)
            else:
                print(i, result)
        else:
            print(i, result)
        if isSuccess == True:  # if geocoding is successful,
            # store the results
            lat.append(result[0])  # latitude
            lng.append(result[1])  # longitude
    return lat, lng


# call the geocoding function
[lat,lng]=GeocodeStreetLocationCity(data)

# we put the list of latitude,longitude into pandas data frame
df = pd.DataFrame(
    {'latitude': lat,
     'longitude': lng
    })

# do geocode for the whole mega city
geocode_result = gm.geocode('Metro Manila')[0]  # change the name into your city of interest

# get the center of the city
center_lat=geocode_result['geometry']['location']['lat']
center_lng=geocode_result['geometry']['location']['lng']
print('center=',center_lat,center_lng)

# get the bounding box of the city i.e. Metro Manila
bounding_box = geocode_result['geometry']['bounds']
lat_boundary = [bounding_box['southwest']['lat'], bounding_box['northeast']['lat']]
lng_boundary = [bounding_box['southwest']['lng'], bounding_box['northeast']['lng']]
print('boundary:',lat_boundary,lng_boundary)

# remove the list that is outside of the city bounding box
mask=(df.latitude>lat_boundary[0])  & \
     (df.latitude<lat_boundary[1])  & \
     (df.longitude>lng_boundary[0]) & \
     (df.longitude<lng_boundary[1])
df=df[mask]

# add frequency of accidents in the location
df['weight']=1

# save into csv file
df.to_csv('locations.csv')
print('saved gocoded locations to "locations.csv"')




