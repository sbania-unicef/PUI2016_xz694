from __future__ import print_function
import json
import urllib2
import sys

def buslive(mtaApiKey, busLine):
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaApiKey, busLine)
	response = urllib2.urlopen(url)
	data = response.read().decode("utf-8")
	jsonData = json.loads(data)
	busActivity = jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	busCount = len(busActivity)
	
	print ("Bus Line : %s \nNumber of Active Buses : %d"%(busLine, busCount))

	for n in range(busCount):
		busLat = busActivity[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		busLon = busActivity[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print ("Bus", n, "is at latitude %f and longitude %f"%(busLat, busLon))

buslive(sys.argv[1], sys.argv[2])