#!/bin/bash

# read sensors

/usr/bin/digitemp_DS9097 -c /etc/digitemprc -q -t0 -o "%Y-%m-%d %H:%M:%S Sensor %s C: %.2C F: %.2F" >> /home/pi/Documents/Temperature/temperature.log
/usr/bin/digitemp_DS9097 -c /etc/digitemprc -q -t0 -o "%Y-%m-%d %H:%M:%S" > /home/pi/Documents/Temperature/current_temperature_time.txt
/usr/bin/digitemp_DS9097 -c /etc/digitemprc -q -t0 -o "%.2C" > /home/pi/Documents/Temperature/current_temperature.txt

# create history graph

gnuplot /home/pi/Documents/Temperature/plotinfile.dat

# upload files

sshpass -p "passwd" scp /home/pi/Documents/Temperature/current_temperature.txt username@x.y.z.d:/www/temperature_local.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/current_temperature_time.txt username@x.y.z.d:/www/temperature_time_local.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperature.log username@x.y.z.d:/www/temperature_local.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturehistory.gif username@x.y.z.d:/www/temperature_local_history.gif
