import subprocess as sub
import sys

#prints all the information about the available wireless networks out. 
def searchWirlessNetworks():
    out = sub.Popen(['sudo', 'iwlist', 'wlan0', 'scan' ],stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print output

#ENTRY POINT
if __name__ == "__main__":
   searchWirlessNetworks()
