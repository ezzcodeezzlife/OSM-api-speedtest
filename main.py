import requests
import time
from datetime import datetime

URLS = ["https://lz4.overpass-api.de/api/interpreter", "https://z.overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter", "https://overpass.openstreetmap.ru/api/interpreter", "https://overpass.openstreetmap.fr/api/interpreter"]
DATASTRING = '?data=[out:json];(node[%27amenity%27=%27bench%27](50.22364307664712,8.449115594560567,50.24036141038248,8.46567765838438);node[%27leisure%27=%27picnic_table%27](50.22364307664712,8.449115594560567,50.24036141038248,8.46567765838438););out%20body;'
print("Script started..")
while True:

    for URL in URLS:
        url = URL + DATASTRING

        try:
            r = requests.get(url)
            statuscode = r.status_code
            timestamp = datetime.now()
            elapsedtime = r.elapsed.total_seconds()
            print("<{}> in {} at {} from {}".format(statuscode, elapsedtime, timestamp, URL))
            time.sleep(1) #29 min
        except Exception as e:
            print(e)

    
    time.sleep(60) #29 min
