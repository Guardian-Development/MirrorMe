# MirrorMe
A wireless mirroring service for the Raspberry Pi 3, aimed for learning purposes only.

#Set Up
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install dnsmasq hostapd

Restart your Pi to let changes take affect.

#Configure your Pi as a Router
sudo python mirrorme.py configure

restart your pi

sudo service hostapd start

sudo service dnsmasq start 
