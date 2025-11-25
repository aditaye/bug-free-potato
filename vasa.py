from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64
aga = "aHR0cHM6Ly93d3cudHdpdGNoLnR2L2JydXRhbGxlcw=="
decoded_bytes = base64.b64decode(aga)
url = decoded_bytes.decode("utf-8")
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as gret:
    gret.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    gret.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )

    gret.uc_open_with_reconnect(url, 5)
    gret.sleep(14)
    if gret.is_element_present("#live-channel-stream-information"):
    
        if gret.is_element_present('button:contains("Accept")'):
            gret.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            gret2 = gret.get_new_driver(undetectable=True)
            gret2.uc_open_with_reconnect(url, 5)
            gret2.sleep(10)
            if gret2.is_element_present('button:contains("Accept")'):
                gret2.uc_click('button:contains("Accept")', reconnect_time=4)
            while gret2.is_element_present("#live-channel-stream-information"):
                gret2.sleep(120)
            gret.quit_extra_driver()
