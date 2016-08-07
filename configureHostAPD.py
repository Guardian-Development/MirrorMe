import os
import sys
import fileinput

def configure(name, password):
    filedata = None
    pathName = '/home/pi/Documents/Python Projects/testHostapd.txt'
    newWifiName = "ssid=" + name
    newWifiPassword = "wpa_passphrase=" + password

    #check file path exists. 
    if not os.path.isfile(pathName):
       print("file doesn't exist")
       sys.exit(1)

    #open the file and read contents
    with open(pathName, 'r') as file:
        filedata = file.read()
        print("reading file...")

    #make updates to the file that we require.
    print("making changes...")
    filedata = filedata.replace('ssid=wifi', newWifiName)
    filedata = filedata.replace('wpa_passphrase=YourPassPhrase',
                                newWifiPassword)

    #write changes back to file
    with open(pathName, 'w') as file:
        file.write(filedata)
        print("changes made")
