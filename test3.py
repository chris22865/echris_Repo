
# to handle csv files
import csv
# for GET and POST requests
import requests
# or maybe import urllib.request
import os.path

# for dates and times that uploads/downloads occur
from datetime import datetime

def etldrop():
	# get current time and set function to call
	date = datetime.utcnow()
	filename = date.strftime('sensordata_%Y_%m_%d_%H.csv')
	# declare web endpoint with singular var and parse out diff dates plus set filetype as .csv
	URL = "https://russellthackston.me/etl/" + filename 
	# store everything after the 4th slash only
	justSensorFile = URL.split('/')[4]
	sensordata = requests.get(URL).text
	
	# break the file into lines (split it by "\r\n")
	sensordatalines = sensordata.split('\n')
	linesToSend = [sensordatalines.pop(0)]
	for line in sensordatalines:
		fields = line.split(',')
		if len(fields) == 4:
			print(float(fields[3]) < 5.0)
			print(' ')
			if float(fields[3]) < 5.0:
				#append linesToSend
				linesToSend.append(line)
				
	linesToSend = '\n'.join(linesToSend)
	print(linesToSend)
	
	# next join all TRUES with linesToSend
	
	
	
	
	
	# make a new array containing only the first line (with the header stuff in it)
	# for each line, break the line into fields by comma (split)
	# for line in sensordatalines:
	# 	SplitData = line.strip()
	# 	print(SplitData)
	# 	print(' ')
		
	#	SplitData = line.split()
	#	print(SplitData)

		#SplitData = line.split(',')
		#print(SplitData)
	
	# if the fourth field (the battery charge) is less than 5.0
	
		#SplitData = line.split(',')[4]
		#print(SplitData)
	
	# add it to the array
	# set fileToSend equal to that new csv
	
	r = requests.post('https://russellthackston.me/etl-drop/index.php', headers = {'Authorization':'55658d426732a4fb1f3715cff0cd4056'}, files = {filename: linesToSend})
	print(r.text)
	

etldrop()

 
'''
# check if POST request was succesful
	if etldrop.status_code == requests.codes.ok:
		# Request Successful...
'''
 


'''
SOURCES:

CALL DATETIME
https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python


GET vs POST
https://www.geeksforgeeks.org/get-post-requests-using-python/


PANDAS 
https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

PANDAS READ vs WRITE CSV
https://www.youtube.com/watch?v=NiOPFFmHkVA


CHECK Request
https://stackoverflow.com/questions/43071816/how-to-check-if-request-post-has-been-successfully-posted
'''
