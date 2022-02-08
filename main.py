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
    return parser.parse(timeIN)

def blandford():
    payload={}
    headers = {}
    url = "https://api-v3.mbta.com/predictions?filter[stop]=70149"
    response = requests.request("GET", url, headers=headers, data=payload).text
    parsed = json.loads(response)
    key2 = parsed['data']
    for entry in key2:
        arrival_time = entry['attributes']['arrival_time']
        tmpIndex = arrival_time.index('T')
        cleanTime = arrival_time[tmpIndex+1 : arrival_time.index('-',tmpIndex)]
        a = timeConvert(cleanTime)
        print(a.strftime('%I:%M %p')) #could do %S after the %M for seconds
    
def harvard():
    payload={}
    headers = {}
    url = "https://api-v3.mbta.com/predictions?filter[stop]=1302"
    response = requests.request("GET", url, headers=headers, data=payload).text
    parsed = json.loads(response)
    key2 = parsed['data']
    for entry in key2:
        arrival_time = entry['attributes']['arrival_time']
        tmpIndex = arrival_time.index('T')
        cleanTime = arrival_time[tmpIndex+1 : arrival_time.index('-',tmpIndex)]
        a = timeConvert(cleanTime)
        print(a.strftime('%I:%M %p')) #could do %S after the %M for seconds
    



blandford()










