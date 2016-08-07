import os
import sys
import fileinput
import subprocess as sub

def configure():
    makeChangesDHCPConf()
    makeChangesISCDHCPServer()
    makeChangeInterface()

#configure fliles for DHCP the service responsible for assigning addresses to devices on the network. 
def makeChangesDHCPConf():
    filedata = None
    pathName = '/home/pi/Documents/Python Projects/testText.txt'
    usingSubnet= 'subnet 192.168.10.0 netmask 255.255.255.0 {\r\n range 192.168.10.10 192.168.10.20;\r\n option broadcast-address 192.168.10.255;\r\n option routers 192.168.10.1;\r\n default-lease-time 600;\r\n max-lease-time 7200;\r\n option domain-name \"local-network\";\r\n option domain-name-servers 8.8.8.8, 8.8.4.4;\r\n}'

    #check file path exists. 
    if not os.path.isfile(pathName):
        print("file doesn't exsist")
        sys.exit(1)

    #open the file and read in contents. 
    with open(pathName, 'r') as file:
        filedata = file.read()
        print("reading file..")

    #make updates to the file that we require
    print("making changes...")
    filedata = filedata.replace('#authoritative;', 'authoritative;')
    filedata = filedata.replace('option domain-name "example.org";',
                                '#option domain-name "example.org";')
    filedata = filedata.replace('option domain-name-servers ns1.example.org, ns2.example.org;',
                                '#option domain-name-servers ns1.example.org, ns2.example.org;')

    #write changes back. 
    with open(pathName, 'w') as file:
        file.write(filedata)
        print("changes made")

    #append file with network addresses we will serve to users.
    with open(pathName, 'a') as file:
        file.write(usingSubnet)
        print("subnet added")

#make the DHCP server hand out addresses on the wireless interface. 
def makeChangesISCDHCPServer():
    filedata = None
    pathName = '/home/pi/Documents/Python Projects/testServer.txt'

    #check file path exists
    if not os.path.isfile(pathName):
        print("file doesn't exsist")
        sys.exit(1)

    #open the file and read from it.
    with open(pathName, 'r') as file:
        filedata = file.read()
        print("reading file...")

    #update the file
    print("making changes...")
    filedata = filedata.replace('INTERFACES=""', 'INTERFACES="wlan0"')

    #write changes back
    with open(pathName, 'w') as file:
        file.write(filedata)
        print("changes made")

#Brings down your wireless card to make changes to the interfaces file. 
def makeChangeInterface():

    pathNameOld = '/home/pi/Documents/Python Projects/testInterfaces.txt'
    pathNameNew = './interfaces.txt'
    filedata = None
    
    #make Linux command call to make sure WLAN interface is down. 
    out = sub.Popen(['sudo', 'ifdown', 'wlan0'],stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = out.communicate()
    print("wireless interface down")

    #check files exists
    if not os.path.isfile(pathNameOld):
        print("can't find original interface")
        sys.exit(1)
    if not os.path.isfile(pathNameNew):
        print("can't find new interfaces file")
        sys.exit(1)

    print("files all exist") 
    #open new file and read from it
    with open(pathNameNew, 'r') as file:
        filedata = file.read()
        print("reading new interfaces file.")

    #write contents to old file replacing it
    with open(pathNameOld, 'w') as file:
        file.write(filedata)
        print("overwritten interfaces file")


    #Enable NAT (allows internet access)
    #open file
    #scroll down to last line and add code

    #run command to start router

    #set up translation between ethernet port and wireless card.

    #start wireless router

    #provide persistance of network (maybe this is optional flag) 
    
