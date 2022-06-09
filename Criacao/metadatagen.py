from datetime import datetime, timedelta
import json


lista =[]
d=365
for x in range (0,d):
    lista.append((datetime(2022, 12, 31) - timedelta(days=x)).strftime("%Y-%m-%d"))     #create array of dates / establish first date


cidades=["New York", "Boston", "Madrid", "Washington DC", "San Francisco", "London", "Toronto", "Dublin", "Mexico City", "Chicago", "Los Angeles", "Paris", "Vienna", "Stockholm", "Zurich", "Helsinki", "Kyiv", "Cairo", "Tel Aviv", "Beijing", "Shanghai", "Seoul", "Singapore", "Tokyo", "Hong Kong", "Moscow", "Sydney", "Cape Town", "Rio de Janeiro"] #cities
clat=["40.7128", "42.3601", "40.4168","38.9072", "37.7749", "51.5072","43.6532","53.3498","19.4326", "41.8781", "34.0522", "48.8566", "48.2082","59.3293","47.3769","60.1699","50.4501","30.0444", "32.0853","39.9042","31.2304","37.5665","1.3521","35.6762","22.3193","55.7558","-33.8688","-33.9249","-22.9068"] #lat coordinates
clon= ["-74.0060", "-71.0589","-3.7038","-77.0369","-122.4194","-0.1276", "-79.3832", "-6.2603","-99.1332", "-87.6298", "-118.2437", "2.3522", "16.3738","18.0686","8.5417", "24.9384","30.5234","31.2357", "34.7818","116.4074","121.4737","126.9780","103.8198","139.6503","114.1694","37.6173","151.2093","18.4241","-43.1729"] #lon coordinates

cnt = 0
for i in range (0,d):

    for j in range (0,len(cidades)):
        
        
        data = {
        "description": "This is the skymap for " + cidades[j] + ", specifically at coordinates " + clat[j]+"/"+clon[j] + ", at 23:59 on the date " + lista[i] , 
        "image": "ipfs://QmZC2GS5EeQgS6Eab96HT9Nrrkxs8M2FyAzE9nrSFtNSHA/2022-"+lista[i][5:7]+"-"+lista[i][-2:]+"%20"+cidades[j]+".png",        
        "name": lista[i]+" "+cidades[j],
        "attributes": [
            {
                "trait_type": "Month",
                "value": lista[i][5:7]
            },
            {
                "trait_type": "Day",
                "value": lista[i][-2:]
            },
            {
                "trait_type": "City",
                "value": cidades[j]
            }
        ] 
        }
        cnt = cnt + 1
        with open(str(cnt)+".json", "w") as write_file:
            json.dump(data, write_file, indent=True)




