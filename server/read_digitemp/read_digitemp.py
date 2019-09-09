# Tuomas Eerola - 2019
# Python3 script
# requires sys, datetime, influxdb

import os
import sys
from influxdb import InfluxDBClient

def processsensor(database, sensor_id, sensor_location="Unknown", calibration=0):

  print ("==== This script reads the local 1-wire sensor")
  print ("==== " + sensor_id)
  print ("====")

  if (database != "-t"):
    print ("Error: This scripts supports temperature only.")
    sys.exit()

# read sensors

  digitemp_commands = []
  digitemp_commands.append('/usr/bin/digitemp_DS9097 -c /etc/digitemprc -q -t0 -o "%.2C"')

  for i in digitemp_commands:
    output = os.popen(i).read().rstrip('\n')
    if (output == ""):
      print("Error: Error reading 1-wire.")
      sys.exit()
    print("Temperature =  " + output + " Celsius")

    points = []

    point = {
                'measurement': "temp",
                'tags': {
                    'dev': sensor_id,
                },
                'fields': {
                    'value': float(output),
                },
            }

    points.append(point)

    print(points)

    client = InfluxDBClient(host='a.b.c.d', 
                            port=8086, 
                            database='temperature')
    client.write_points(points)


processsensor("-t","d5")
