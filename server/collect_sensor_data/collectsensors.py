# Tuomas Eerola - 2019
# Python3 script
# requires os, sys, readsensorlist, processsensor

print ("==== This script reads the sensors listed in sensorlist.csv")
print ("==== and publishes the data on a web server.")

import os
import sys
import readsensorlist
import processsensor

server_conf_file = "./server.conf"
sensor_conf_file = "./sensorlist.csv"

sensors=readsensorlist.readsensorlist(sensor_conf_file)

numsensors = len(sensors)

if (numsensors == 0):
  print ("Invalid sensorlist.csv")
  sys.exit()

output_files = []

for i in range(numsensors):
  items = len(sensors[i])
  if (items < 3):
    print ("Invalid sensorlist.csv")
    sys.exit()

  if (sensors[i][2] == "temperature"):
    database = "-t"
  else:
    database = "-h"

  if (items < 4):
    calibration = 0
  else:
    calibration = sensors[i][3]

  output_files.append(processsensor.processsensor(database,sensors[i][0],sensors[i][1],calibration))

output_files.append(processsensor.processindooraverage())

server_data = [line.rstrip('\n') for line in open(server_conf_file)]

for item in output_files:
  for file in item:
    print(file)
    head, tail = os.path.split(file)
    upload_command = ("sshpass -p \"" + server_data[3] + "\" scp " + file + " " + server_data[2] + "@" + server_data[0] + ":" + server_data[1] + tail)
    output = os.popen(upload_command).read()
    print(upload_command)
