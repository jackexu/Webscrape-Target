#!/usr/bin/env python
# coding: utf-8
# Author: @jackexu https://github.com/jackexu

import pandas as pd
import requests
import time

## Input your zipcode and the product ID
my_location = 'xxxxx'
product_id = '77464001' #Nintendo Switch with Neon Blue and Neon Red Joy-Con

## Build Connection
s = requests.session()
s.get('https://www.target.com');
key = s.cookies['visitorId']

## Get/Input store id
location_info = requests.get('https://redsky.target.com/v3/stores/nearby/%s?key=%s&limit=1&within=100&unit=mile'
                             %(my_location, key)).json()
my_store_id = location_info[0]['locations'][0]['location_id']
## you can set to the store you want to check: use below and comment out above get store id part
# my_store_id = xxxx

## Accquire data
url = 'https://redsky.target.com/web/pdp_location/v1/tcin/%s' % product_id
payload = {'pricing_store_id': my_store_id, 'key': key}
target_var = 'msrp'

## Main
while True:
    # Get json and convert to df
    jsonData = requests.get(url, params=payload).json()
    df = pd.DataFrame(jsonData['price'], index=[0])
    # If there is no 'msrp', then not available
    if target_var in df.columns:
        print('\nYeah!! Available now!!')
        # Can add sending email function here

        break
    else:
        print('\nStill not available :( ')
        time.sleep(300)  ## run every 5 seconds
