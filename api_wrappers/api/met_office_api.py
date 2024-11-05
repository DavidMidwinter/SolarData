from settings import WEATHER_DATA_API_KEY, WEATHER_DATA_URL
import requests
import sys
import logging as log
import time

# Code from https://github.com/MetOffice/weather_datahub_utilities/blob/main/site_specific_download/ss_download.py,
# 2023 (C) Crown Copyright, Met Office. All rights reserved.

def retrieve_forecast(latitude, longitude, timesteps="hourly", excludeMetadata=True, includeLocation=True):
    url = WEATHER_DATA_URL + timesteps

    headers = {'accept': "application/json",
               "apikey": WEATHER_DATA_API_KEY}
    params = {
        'excludeParameterMetadata': excludeMetadata,
        'includeLocationName': includeLocation,
        'latitude': latitude,
        'longitude': longitude
    }

    success = False
    retries = 5

    while not success and retries > 0:
        try:
            req = requests.get(url, headers=headers, params=params)
            success = True
        except Exception as e:
            log.warning("Exception occurred", exc_info=True)
            retries -= 1
            time.sleep(10)
            if retries == 0:
                log.error("Retries exceeded", exc_info=True)
                sys.exit()

    req.encoding = 'utf-8'

    return req

