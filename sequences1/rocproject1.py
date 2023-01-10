# Logic Framework in Python
#
# Hard-coded Timer:
import time
time.sleep(60*60)
# Recommend OS's built in task scheduler e.g. Window Task Scheduler's Cron Job "Scheduled Task"

# Query Cavok API to get JSON response, from which data can be extracted + temporarily saved
# Note built in JSON decoder in requests library
import requests
page = requests.get('http://<Cavok Server IP>:<Cavok Server Port Number>/tracks')
data = page.json()

# Alternative method using JSON, urllib libraries
import json
import urllib.request
page = urllib.request.urlopen(http://<Cavok Server IP>:<Cavok Server Port Number>/tracks)
data = page.read()
encoding = page.info().get_content_charset('utf-8')
json.loads(data.decode(encoding))


# JSON response decoded and converted into string/dictionary/array
# Extraction logic goes here, then save position data e.g. coordinatedatavariable
# Can add logic to compare position data for all relevant aircraft
# and add caution message if two aircraft are within set distance/altitude of each other



# Method 1: Save to text file
open('temporarytextfile', 'w') as z:
    z.write(coordinatedatavariable\n)
    z.write(altitude)
    z.write(cautionmessage)

# mIRC Script to read + send message from text file:
on *:start: .temporarytextfile 60 0 temporarytextfile

alias temporarytextfile {
    set -l %filepath temporarytextfile.txt
    if ($file(%filepath).mtime != %temporarytextfile) {
        set %temporarytextfile $file(%filepath).mtime
        msg #channelname ($read(%filepath)
    }
}


# Partial of Method 2 mIRC DDE to connect to IRC server:
# Can potentially modify for SendMessage() method
# More research required for this method

import socket, string, time, thread
SERVER = “ ”
PORT = ####
NICKNAME = “ “
CHANNEL = “ “

def main():
    global IRC
    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IRC.connect((SERVER, PORT))
    thread.start_new_thread(Listener(),("Thread No:1",2))

def send_data(command):
    IRC.send(command + coordinatedatavariable)

// framework for named python bot to listen for mIRC input
def Listener():
    send_data('USER ___')
    send_data('NICK ___')
    while (1):
        buffer = IRC.recv(1024)
        msg = string.split(buffer)
        if msg[0] == "PING":
            print 'Pinged!'
        IRC.send("PONG %s" % msg[1] + '\n')
