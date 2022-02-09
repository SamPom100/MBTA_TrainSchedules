import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

'''
https://api-v3.mbta.com/docs/swagger/index.html#/

api_key = '61d93f**********3'


see dump.json


'''

from distutils.command.clean import clean
import string
import requests
import json
from datetime import datetime
from dateutil import parser

def prettyPrint(printIN: str):
    print(json.dumps(printIN, indent=4, sort_keys=True))

def timeConvert(timeIN: str):
    return parser.parse(timeIN).strftime('%I:%M:%S %p') #could do %S after the %M for seconds
    
def getTimes(stopID: int):
    toReturn = []
    url = "https://api-v3.mbta.com/predictions?filter[stop]="+str(stopID)
    response = requests.request("GET", url, headers={}, data={}).text
    parsed = json.loads(response)
    for entry in parsed['data']:
        arrival_time = entry['attributes']['arrival_time']
        tmpIndex = arrival_time.index('T')
        cleanTime = arrival_time[tmpIndex+1 : arrival_time.index('-',tmpIndex)]
        timeObject = parser.parse(cleanTime)
        now = datetime.now()
        diff = timeObject - now
        arrivalStr = ''
        if(timeObject < now):
            arrivalStr = 'passed'
        else:
            arrivalStr = str(round(diff.total_seconds()/60,2)) + " minutes"
        toReturn.append(timeObject.strftime('%I:%M %p') +"  -->  "+arrivalStr)
    return toReturn

def harvard():
    for x in getTimes(70130):
        print(x)

def blandford():
    for x in getTimes(70149):
        print(x)

def printBoth():
    print('\n')
    print("--------- Harvard ---------")
    harvard()
    print('\n\n')
    print("--------- Blandford ---------")
    blandford()
    print('\n')



printBoth()







