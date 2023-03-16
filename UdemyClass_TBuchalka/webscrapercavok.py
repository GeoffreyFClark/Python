import time
time.sleep(60*60)      #Note 60*60 refers to seconds the program will idle

#timer

import json
import urllib.request
page = urllib.request.urlopen(http://<Cavok Server IP>:<Cavok Server Port Number>/tracks)
data = page.read()
encoding = page.info().get_content_charset('utf-8')
json.loads(data.decode(encoding))

#or

import requests
page = requests.get(http://<Cavok Server IP>:<Cavok Server Port Number>/tracks)
data = page.json()



