import os
import sys
import fileinput
import subprocess as sub

def execute():
    configureInterfaces()
    configureStaticIP()
    restartServices()
    print "completed configuringInterfaces.py"

def configureInterfaces():
    filedata = None
    pathName = '/etc/dhcpcd.conf'
    addedLine = 'denyinterfaces wlan0'

    #check file path exists.
    if not os.path.isfile(pathName):
        print "file does not exist for /etc/dhcpcd.conf"
        sys.exit(1)

    #open the file and read contents
    with open(pathName, 'a') as file:
        file.write(addedLine)
        print "added denyinterfaces wlan0 to dhcpcd.conf"

    print"complete configureInterfaces"

def configureStaticIP():
    filedata = None
    pathNameOld = '/etc/network/interfaces'
    pathNameNew = '.newFiles/interfaces.txt'

    #check the file exists
    if not os.path.isfile(pathNameOld):
        print "can't find the file for interfaces"
        sys.exit(1)
    if not os.path.isfile(pathNameNew):
        print "can't find the new interfaces file"
        sys.exit(1)

    #open the new file and read the data
    with open(pathNameNew, 'r') as file:
        filedata = file.read()
        print "reading new interfaces file"

    #write contents to old file replacing it
    with open(pathNameOld, 'w') as file:
        file.write(filedata)
        print "overwritten the interfaces file"

    print "make changes to the interfaces file complete"

def restartServices():
    out = sub.Popen(['sudo', 'service', 'dhcpcp', 'restart'], stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print output
    print errors
    print "dhcpcd restarted"

    out = sub.Popen(['sudo', 'ifdown', 'wlan0'], stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print output
    print errors
    
    out = sub.Popen(['sudo', 'ifup', 'wlan0'], stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print output
    print errors
