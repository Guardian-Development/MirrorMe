import subprocess as sub
import sys
import re

#prints all the information about the available wireless networks out. 
def searchWirelessNetworks():

    #make Linux command call to list WiFi networks. 
    out = sub.Popen(['sudo', 'iwlist', 'wlan0', 'scan' ],stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()

    #search output using REGEX to find ESSID names to show to user. 
    pattern = r'\bESSID\b\:\"[^.]*\"'
    regex = re.compile(pattern, re.IGNORECASE)
    for match in regex.finditer(output):
        print match.group(0)
    print("complete search")
