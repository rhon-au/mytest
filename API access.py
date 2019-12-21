import requests 
city = "london"

# Sample data for the the city of london
urlx="https://samples.openweathermap.org/data/2.5/weather?q="+city+"&appid=b6907d289e10d714a6e88b30761fae22"

# send the reqest to the URL using the Get method
r = requests.get(url = urlx)
output = r.json()

# parse the information from the return JSON
print ("Raw JSON \n")
print (output)
print ("\n")

#fetch and print Latitude and Longitude
citylatitude = output ['coord'] ['lat']
citylongitude = output ['coord'] ['lon']
print ("Longitude: "+str(citylongitude)+" , "+"Latitude: "+str(citylatitude))
