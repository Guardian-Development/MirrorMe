import subprocess as sub
import sys
import re
import configureISC_DHCP_Server as dhcpConfig
import configureNAT as natConfig
import configureHostAPD as apdConfig
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
        dhcpConfig.configure()
        apdConfig.configure("JoePiNetwork", "password")
        natConfig.configure()
        natConfig.enablePersistantState() 
        
