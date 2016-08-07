# MirrorMe
A wireless mirroring service for the Raspberry Pi 3, aimed for learning purposes only. 

#Set Up 
sudo apt-get install isc-dhcp-server

wget https://github.com/jenssegers/RTL8188-hostapd/archive/v1.1.tar.gz

tar -zxvf v1.1.tar.gz

cd RTL8188-hostapd-1.1/hostapd

sudo make

sudo make install

