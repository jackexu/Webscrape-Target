#!/usr/bin/env python
# coding: utf-8
# Author: @jackexu https://github.com/jackexu

import pandas as pd
import requests

## Build Connection
s = requests.session()
s.get('https://www.target.com');
key = s.cookies['visitorId']
# location = s.cookies['GuestLocation'].split('|')[0]

## Input your zipcode and the product ID
my_location = 'xxxxx'
product_id = '77464001' #Nintendo Switch with Neon Blue and Neon Red Joy-Con
# url = "https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001"

## Get store id
location_info = requests.get('https://redsky.target.com/v3/stores/nearby/%s?key=%s&limit=1&within=100&unit=mile'
                             %(my_location, key)).json()
my_store_id = location_info[0]['locations'][0]['location_id']
# print(store_id)

## Put your store_id here (like 2480, 2325) and run below - can also comment out print above after you have it
# my_store_id = 2480

## Get json and convert to df
url = 'https://redsky.target.com/web/pdp_location/v1/tcin/%s' %product_id

payload = {'pricing_store_id': my_store_id, 'key': key}

jsonData = requests.get(url, params=payload).json()

df = pd.DataFrame(jsonData['price'], index=[0])

## If there is no msrp, then no available
target_var = 'msrp'

if target_var in df.columns:
    print('\nYeah!! Available now!!')
else:
    print('\nStill not available :( ')
