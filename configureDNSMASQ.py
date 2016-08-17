import os
import sys
import fileinput
import subprocess as sub

def execute():
    configureDNSMASQ()

def configureDNSMASQ():
    filedata = None
    newPath = './dnsmasq.conf'
    oldPath = '/etc/dnsmasq.conf'
    
    print "created new dnsmasq conf file"

    if not os.path.isfile(newPath):
        print "new dnsmasq file doesn't exist"
        sys.exit(1)

    with open(newPath, 'r') as file:
        filedata = file.read()
        print "reading new data from file for dnsmasq"
        print filedata

    with open(oldPath, 'w') as file:
        file.write(filedata)
        print "writing new dnsmasq file"

    print "completed dnsmasq configuration"


    
    
