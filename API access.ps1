# use the city of London as a reference
 $city = "london"
 $urlx = "https://samples.openweathermap.org/data/2.5/weather?q="+$city+"&appid=b6907d289e10d714a6e88b30761fae22"
#
#
# used to invoke API using GET method
 $stuff = Invoke-RestMethod -Uri $urlx -Method Get
#
#
# write raw json
 $stuff
#
#
# write the output of latitude and longitude
 Write-Host ("Longitude: "+$stuff.coord.lon+" , "+"Latitude: "+$stuff.coord.lat)

 
