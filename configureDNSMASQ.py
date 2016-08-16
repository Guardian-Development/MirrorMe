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
    
    print "moving old dnsmasq config file"
    
    sub.Popen(['sudo', 'mv', '/etc/dnsmasq.conf',
               '/etc/dnsmasq.conf.orig'],stdout=sub.PIPE, stderr=sub.PIPE)

    sub.Popen(['sudo', 'touch', '/etc/dnsmasq.conf'],stdout=sub.PIPE, stderr=sub.PIPE) 

    print "created new dnsmasq conf file"

    is os.path.isfile(newPath):
        print "new dnsmasq file doesn't exist"
        sys.exit(1)

    with open(newPath, 'r') as file:
        filedata = file.read()
        print "reading new data from file for dnsmasq"

    with open(oldPath, 'w') as file:
        file.write(fileData)
        print "writing new dnsmasq file"

    print "completed dnsmasq configuration"


    
    
