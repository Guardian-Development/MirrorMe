import os
import sys
import fileinput
import subprocess as sub

def configure():
    filedata = None
    pathName = '/home/pi/Documents/Python Projects/testSysctl.txt'

    #check file path exists
    if not os.path.isfile(pathName):
        print("file doesn't exist")
        sys.exit(1)

    #append file with ip forwarding
    with open(pathName, 'a') as file:
        file.write("net.ipv4.ip_forward=1")
        print("ip forwarding added")

    print("start translation for ip..") 
    #make Linux command call to start translation
    sub.Popen(['sudo', 'sh', '-c', '"echo 1 > /proc/sys/net/ipv4/ip_forward"' ],
                    stdout=sub.PIPE, stderr=sub.PIPE)

    print("bringing wirless card back up..")
    #make Linux command call to bring wirless card back up. 
    sub.Popen(['sudo', 'ifup', 'wlan0'],
                    stdout=sub.PIPE, stderr=sub.PIPE)

    #set up translation between ethernet port and wirless card
    print("Setting up translation between ethernet and wireless..")
    sub.Popen(['sudo', 'iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o', '-j', 'MASQUERADE'],
                    stdout=sub.PIPE, stderr=sub.PIPE)
    sub.Popen(['sudo', 'iptables', '-A', 'FORWARD', '-i', 'eth0', '-o', 'wlan0', '-m', 'state',
               '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'],
                    stdout=sub.PIPE, stderr=sub.PIPE)
    sub.Popen(['sudo', 'iptables', '-A', 'FORWARD', '-i', 'wlan0', '-o', 'eth0', '-j', 'ACCEPT'],
                    stdout=sub.PIPE, stderr=sub.PIPE)

    #Start wireless router
    print("wirless router starting..") 
    sub.Popen(['sudo', 'service', 'isc-dhcp-server', 'start'],
                    stdout=sub.PIPE, stderr=sub.PIPE)
    sub.Popen(['sudo', 'service', 'hostapd', 'start'],
                    stdout=sub.PIPE, stderr=sub.PIPE)

def enablePersistantState():
    #last thing to do before attempting for real. 
    
