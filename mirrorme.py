import subprocess as sub
import sys
import re
import configureInterfaces as interfaces
import configureHostAPD as hostAPD
import configureDNSMASQ as DNSMASQ
import configureNAT as NAT
import wirelessScanner as scanner 

#ENTRY POINT
if __name__ == "__main__":

    #NO OP
    if len(sys.argv) < 2:
        print("Please specify a command")
        sys.exit(1)
        
    #SEARCH OPERATION SPECIFIED
    if sys.argv[1] == "search":
        scanner.searchWirelessNetworks()

    #CONFIGURE OPERATION SPECIFIED
    if sys.argv[1] == "configure":
        #interfaces.execute()
        #hostAPD.execute()
        DNSMASQ.execute()
        NAT.execute() 
        
