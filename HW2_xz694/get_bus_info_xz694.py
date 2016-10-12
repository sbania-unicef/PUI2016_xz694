from __future__ import print_function
import json
import urllib2
import sys
import csv
import numpy as np

def busNextStop(mtaApiKey, busLine, csvFullName):
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaApiKey, busLine)
	response = urllib2.urlopen(url)
	data = response.read().decode("utf-8")
	jsonData = json.loads(data)
	busActivity = jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	busCount = len(busActivity)

	dataArray = np.array(["Latitude", "Longitude", "Stop Name", "Stop Status"])
	
	for n in range(busCount):
		busLat = busActivity[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		busLon = busActivity[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		#with help for checking if the key existing. http://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
		if 'OnwardCalls' in busActivity[n]['MonitoredVehicleJourney']:
			stopName = busActivity[n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
			stopStatus = busActivity[n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
		else:
			stopName = "N/A"
			stopStatus = "N/A"

		busArray = np.array([busLat, busLon, stopName, stopStatus])
		
		#http://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html#numpy.vstack
		dataArray = np.vstack((dataArray, busArray))

#with help from https://www.getdatajoy.com/examples/python-data-analysis/read-and-write-a-csv-file-with-the-csv-module
	with open(csvFullName, 'w') as csvfile: 
		writing = csv.writer(csvfile)
		for row in dataArray:
			writing.writerow(row)

#with help from https://docs.python.org/2/library/csv.html
	with open(csvFullName, 'r') as csvfile:
		reading = csv.reader(csvfile)
		for row in reading:
			print (','.join(row))

	csvfile.close()

busNextStop(sys.argv[1], sys.argv[2], sys.argv[3])