Simple Intro to Python
======================

This repository contains notebooks and scripts to help absolute beginners with a gentle introduction to programming using Python. The pedagogical approach is to use computational modeling of real world problems to engage students.

Structure:
----------

Simple example: dance card creation

Raspberry Pi setup notes:

1. Begin with raspbian jessie by downloading this:
 ```https://www.raspberrypi.org/downloads/raspbian/```
    follow instructions here for duplicating disk image:
 ```https://www.raspberrypi.org/documentation/installation/installing-images/mac.md```
 in order to enable ssh for post-Fall 2016 Jessie versions you need to:
 ```
 cd /Volumes/boot/
 touch ssh
 ```

2. Follow these instructions to get wifi set up from the command line:

```https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md```

eventually you get the following ip address on my home network:

```
pi@raspberrypi:~ $ ifconfig
eth0      Link encap:Ethernet  HWaddr b8:27:eb:2f:24:2f
          inet addr:192.168.2.6  Bcast:192.168.2.255  Mask:255.255.255.0
          inet6 addr: fe80::f419:ff4e:149f:3413/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2176 errors:0 dropped:0 overruns:0 frame:0
          TX packets:751 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:272541 (266.1 KiB)  TX bytes:107905 (105.3 KiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:200 errors:0 dropped:0 overruns:0 frame:0
          TX packets:200 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:16656 (16.2 KiB)  TX bytes:16656 (16.2 KiB)

wlan0     Link encap:Ethernet  HWaddr b8:27:eb:7a:71:7a
          inet addr:10.0.1.87  Bcast:10.0.1.255  Mask:255.255.255.0
          inet6 addr: fe80::fb4d:63f4:e851:bb64/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1300 errors:0 dropped:654 overruns:0 frame:0
          TX packets:119 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:265453 (259.2 KiB)  TX bytes:24151 (23.5 KiB)
```

3. Set up VNC following instructions here:
```
https://www.raspberrypi.org/documentation/remote-access/vnc/
```
 Note: for minecraft over VNC, look at these tips:
 ```https://github.com/RealVNC/raspi-preview```

4. install some things into the default python (2.7)

```
sudo pip install --upgrade pip
sudo pip install jupyter
sudo pip install gpio
sudo pip install numpy
sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran # for scipy install
sudo pip install scipy
sudo pip install pandas
```



5. Don't forget to get latest on the raspian distribution:

```
sudo apt-get update
sudo apt-get upgrade
```


The ```pip install jupyter``` command fails because of a pip bug.  Adding a path file seems to work:

```
touch /home/pi/miniconda3/envs/py3/lib/python3.4/site-packages/easy-install.pth
```

6. The rpi.gpio module needs to be installed via conda:

```conda install -c ericmjl rpi.gpio```


TODO:
-----

curriculum outline

