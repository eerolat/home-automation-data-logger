#!/bin/bash

# read new data from influx

curl -G 'http://localhost:8086/query?db=temperature&&pretty=true' --data-urlencode "q=SELECT * FROM temp WHERE dev='d1' GROUP BY * ORDER BY DESC LIMIT 1" > /home/pi/Documents/Temperature/temperaturegarage_newest.json
curl -G 'http://localhost:8086/query?db=temperature&&pretty=true' --data-urlencode "q=SELECT * FROM temp WHERE dev='d2' GROUP BY * ORDER BY DESC LIMIT 1" > /home/pi/Documents/Temperature/temperaturebedroom_newest.json
curl -G 'http://localhost:8086/query?db=temperature&&pretty=true' --data-urlencode "q=SELECT * FROM temp WHERE dev='d3' GROUP BY * ORDER BY DESC LIMIT 1" > /home/pi/Documents/Temperature/temperaturelivingroom_newest.json
curl -G 'http://localhost:8086/query?db=temperature&&pretty=true' --data-urlencode "q=SELECT * FROM temp WHERE dev='d4' GROUP BY * ORDER BY DESC LIMIT 1" > /home/pi/Documents/Temperature/temperaturelibrary_newest.json
curl -G 'http://localhost:8086/query?db=humidity&&pretty=true' --data-urlencode "q=SELECT * FROM humid WHERE dev='d4' GROUP BY * ORDER BY DESC LIMIT 1" > /home/pi/Documents/Temperature/humiditylibrary_newest.json

jq -rM '.results[].series[].values[][0]' /home/pi/Documents/Temperature/temperaturebedroom_newest.json > /home/pi/Documents/Temperature/temperaturebedroom_currenttime_temp.txt
date -f /home/pi/Documents/Temperature/temperaturebedroom_currenttime_temp.txt "+%F %T" | tr -d '\n' > /home/pi/Documents/Temperature/temperaturebedroom_currenttime.txt 
rm /home/pi/Documents/Temperature/temperaturebedroom_currenttime_temp.txt
#echo $(printf "%0.2f\n" $(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/temperaturebedroom_newest.json)) > /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt
sensor_temp=$(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/temperaturebedroom_newest.json)
sensor_calibr=-0.44
real_temp=$(echo $sensor_temp $sensor_calibr | awk '{print $1 + $2}' | awk '{ printf("%.4g\n", $1) }') 
echo $(printf "%0.2f\n" $real_temp) > /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt

jq -rM '.results[].series[].values[][0]' /home/pi/Documents/Temperature/temperaturegarage_newest.json > /home/pi/Documents/Temperature/temperaturegarage_currenttime_temp.txt
date -f /home/pi/Documents/Temperature/temperaturegarage_currenttime_temp.txt "+%F %T" | tr -d '\n' > /home/pi/Documents/Temperature/temperaturegarage_currenttime.txt 
rm /home/pi/Documents/Temperature/temperaturegarage_currenttime_temp.txt
sensor_temp=$(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/temperaturegarage_newest.json)
sensor_calibr=1.40
real_temp=$(echo $sensor_temp $sensor_calibr | awk '{print $1 + $2}' | awk '{ printf("%.4g\n", $1) }') 
echo $(printf "%0.2f\n" $real_temp) > /home/pi/Documents/Temperature/temperaturegarage_currenttemp.txt

jq -rM '.results[].series[].values[][0]' /home/pi/Documents/Temperature/temperaturelivingroom_newest.json > /home/pi/Documents/Temperature/temperaturelivingroom_currenttime_temp.txt
date -f /home/pi/Documents/Temperature/temperaturelivingroom_currenttime_temp.txt "+%F %T" | tr -d '\n' > /home/pi/Documents/Temperature/temperaturelivingroom_currenttime.txt 
rm /home/pi/Documents/Temperature/temperaturelivingroom_currenttime_temp.txt
sensor_temp=$(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/temperaturelivingroom_newest.json)
sensor_calibr=-0.05
real_temp=$(echo $sensor_temp $sensor_calibr | awk '{print $1 + $2}' | awk '{ printf("%.4g\n", $1) }') 
echo $(printf "%0.2f\n" $real_temp) > /home/pi/Documents/Temperature/temperaturelivingroom_currenttemp.txt

jq -rM '.results[].series[].values[][0]' /home/pi/Documents/Temperature/temperaturelibrary_newest.json > /home/pi/Documents/Temperature/temperaturelibrary_currenttime_temp.txt
date -f /home/pi/Documents/Temperature/temperaturelibrary_currenttime_temp.txt "+%F %T" | tr -d '\n' > /home/pi/Documents/Temperature/temperaturelibrary_currenttime.txt 
rm /home/pi/Documents/Temperature/temperaturelibrary_currenttime_temp.txt
sensor_temp=$(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/temperaturelibrary_newest.json)
sensor_calibr=-0.80
real_temp=$(echo $sensor_temp $sensor_calibr | awk '{print $1 + $2}' | awk '{ printf("%.4g\n", $1) }') 
echo $(printf "%0.2f\n" $real_temp) > /home/pi/Documents/Temperature/temperaturelibrary_currenttemp.txt

jq -rM '.results[].series[].values[][0]' /home/pi/Documents/Temperature/humiditylibrary_newest.json > /home/pi/Documents/Temperature/humiditylibrary_currenttime_temp.txt
date -f /home/pi/Documents/Temperature/humiditylibrary_currenttime_temp.txt "+%F %T" | tr -d '\n' > /home/pi/Documents/Temperature/humiditylibrary_currenttime.txt 
rm /home/pi/Documents/Temperature/humiditylibrary_currenttime_temp.txt
sensor_temp=$(jq -M '.results[].series[].values[][1]' /home/pi/Documents/Temperature/humiditylibrary_newest.json)
sensor_calibr=0
real_humidity=$(echo $sensor_temp $sensor_calibr | awk '{print $1 + $2}' | awk '{ printf("%.4g\n", $1) }') 
echo $(printf "%0.2f\n" $real_humidity) > /home/pi/Documents/Temperature/humiditylibrary_currenthumid.txt

#calculate average indoor temperature

bedroom=0
livingroom=0
kitchen=0
library=0
total=0
average=0

rooms=4
bedroom=$(cat /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt)
livingroom=$(cat /home/pi/Documents/Temperature/temperaturelivingroom_currenttemp.txt)
library=$(cat /home/pi/Documents/Temperature/temperaturelibrary_currenttemp.txt)

kitchen_temp="$(curl http://eerola.dy.fi/temp/temperaturein.txt)"

kitchen=$(echo $kitchen_temp | awk '{print $1}')

total=$(echo $bedroom $livingroom $kitchen $library | awk '{print $1 + $2 + $3 + $4}')
average_temp=$(echo $total $rooms | awk '{print $1 / $2}' | awk '{ printf("%.4g\n", $1) }')
average=$(printf "%0.2f\n" $average_temp)

echo $average "C" > /home/pi/Documents/Temperature/temperatureinaverage_currenttemp.txt

#create local logs and format datetimes for gnuplot

cat /home/pi/Documents/Temperature/temperaturebedroom_currenttime.txt | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturebedroom.log
echo " Sensor 0 C: " | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturebedroom.log
cat /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt >> /home/pi/Documents/Temperature/temperaturebedroom.log
#echo -n "C"  >> /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt

cat /home/pi/Documents/Temperature/temperaturegarage_currenttime.txt | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturegarage.log
echo " Sensor 0 C: " | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturegarage.log
cat /home/pi/Documents/Temperature/temperaturegarage_currenttemp.txt >> /home/pi/Documents/Temperature/temperaturegarage.log
#echo -n "C"  >> /home/pi/Documents/Temperature/temperaturegarage_currenttemp.txt

cat /home/pi/Documents/Temperature/temperaturelivingroom_currenttime.txt | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturelivingroom.log
echo " Sensor 0 C: " | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturelivingroom.log
cat /home/pi/Documents/Temperature/temperaturelivingroom_currenttemp.txt >> /home/pi/Documents/Temperature/temperaturelivingroom.log
#echo -n "C"  >> /home/pi/Documents/Temperature/temperaturelivingroom_currenttemp.txt

cat /home/pi/Documents/Temperature/temperaturelibrary_currenttime.txt | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturelibrary.log
echo " Sensor 0 C: " | tr -d '\n' >> /home/pi/Documents/Temperature/temperaturelibrary.log
cat /home/pi/Documents/Temperature/temperaturelibrary_currenttemp.txt >> /home/pi/Documents/Temperature/temperaturelibrary.log

cat /home/pi/Documents/Temperature/humiditylibrary_currenttime.txt | tr -d '\n' >> /home/pi/Documents/Temperature/humiditylibrary.log
echo " Sensor 0 C: " | tr -d '\n' >> /home/pi/Documents/Temperature/humiditylibrary.log
cat /home/pi/Documents/Temperature/humiditylibrary_currenthumid.txt >> /home/pi/Documents/Temperature/humiditylibrary.log


# create history graphs

gnuplot /home/pi/Documents/Temperature/plotinfilegarage.dat
gnuplot /home/pi/Documents/Temperature/plotinfilebedroom.dat
gnuplot /home/pi/Documents/Temperature/plotinfilelivingroom.dat
gnuplot /home/pi/Documents/Temperature/plotinfilelibrary.dat
gnuplot /home/pi/Documents/Temperature/plotinfilelibraryhumidity.dat

# upload files

sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturebedroom_currenttemp.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_bedroom.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturebedroom_currenttime.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_time_bedroom.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturebedroom.log username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_bedroom.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturebedroomhistory.gif username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_bedroom_history.gif

sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturegarage_currenttemp.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_garage.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturegarage_currenttime.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_time_garage.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturegarage.log username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_garage.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturegaragehistory.gif username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_garage_history.gif

sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelivingroom_currenttemp.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_livingroom.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelivingroom_currenttime.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_time_livingroom.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelivingroom.log username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_livingroom.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelivingroomhistory.gif username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_livingroom_history.gif

sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelibrary_currenttemp.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_library.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelibrary_currenttime.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_time_library.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelibrary.log username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_library.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperaturelibraryhistory.gif username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_library_history.gif

sshpass -p "passwd" scp /home/pi/Documents/Temperature/humiditylibrary_currenthumid.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/humidity_library.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/humiditylibrary_currenttime.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/hunidity_time_library.txt
sshpass -p "passwd" scp /home/pi/Documents/Temperature/humiditylibrary.log username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/humidity_library.log
sshpass -p "passwd" scp /home/pi/Documents/Temperature/humiditylibraryhistory.gif username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/humidity_library_history.gif

sshpass -p "passwd" scp /home/pi/Documents/Temperature/temperatureinaverage_currenttemp.txt username@x.y.z.d:/mnt/HD/HD_a2/ffp/opt/srv/www/pages/temp/temperature_inaverage.txt
