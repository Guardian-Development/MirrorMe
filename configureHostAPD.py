import os
import sys
import fileinput
import subprocess as sub

def execute():
    createConfigFile()
    populateConfigFile()
    setupOnBootConfigFile()

def createConfigFile():
    out = sub.Popen(['sudo', 'touch', '/etc/hostapd/hostapd.conf'], stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print errors
    print "completed creating the hostapd.conf file (empty)"

def populateConfigFile():
    filedata = None
    pathNameOld = '/etc/hostapd/hostapd.conf'
    pathNameNew = './hostapdconfig.txt'

    #check file exists
    if not os.path.isfile(pathNameNew):
        print "can't find hostapd.conf file"
        sys.exit(1)
    if not os.path.isfile(pathNameOld):
        print "can't find the old hostapd.conf file"
        sys.exit(1)

    #write to file
    with open(pathNameNew, 'r') as file:
        filedata = file.read()
        print "reading new hostapd conf file"

    with open(pathNameOld, 'w') as file:
        file.write(filedata)
        print "overwritten the hostapd conf file"

    print "populated config file complete"

def setupOnBootConfigFile():
    filedata = None
    pathName = '/etc/default/hostapd'

    #check file path exists
    if not os.path.isfile(pathName):
        print "can't find the default hostapd file"
        sys.exit(1)

    with open(pathName, 'r') as file:
        filedata = file.read()
        print "reading hostapd default file"

    print "making changes to the default hostapd file"

    filedata = filedata.replace('#DAEMON_CONF=""', 'DAEMON_CONF="/etc/hostapd/hostapd.conf"')

    with open(pathName, 'w') as file:
        file.write(fileData)
        print "completed writing to hostapd default file"

    print "completed the setup of the boot config file"

    
        






    
