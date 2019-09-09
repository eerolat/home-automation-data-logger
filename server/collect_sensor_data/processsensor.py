# Tuomas Eerola - 2019
# Python3 script
# requires sys, datetime, readinfluxdata

import sys
from datetime import datetime
import readinfluxdata


def processsensor(database, sensor_id, sensor_location, calibration=0):

  print ("==== This script coordinates the reading of")
  print ("==== sensor " + sensor_id + " data")
  print ("====")

  influxdata=readinfluxdata.readinfluxdata(database,sensor_id)

  measurement_data = "{:.2f}".format(influxdata[0]-float(calibration))
  measurement_time = datetime.fromtimestamp(influxdata[1])

  #
  # Write out data files
  #

  output_files = []

  if (database == '-h'):
    data_type="humidity"
  elif (database == '-t'):
    data_type="temperature"
  else:
    print("Usage: " + script_name + "[-ht] sensor_id sensor_location gnuplot_file")
    print("Please use -h for humidity data, -t for temperature data.")
    sys.exit()

  out_file=("./data/" + data_type + sensor_location + "_currentdata.txt")
  f=open(out_file,"w+")
  if (data_type=="humidity"):
    f.write(str(measurement_data))
  else:
    f.write(str(measurement_data) + " C")
  f.close()
  output_files.append(out_file)

  out_file=("./data/" + data_type + sensor_location + "_currenttime.txt")
  f=open(out_file,"w+")
  f.write(str(measurement_time))
  f.close()
  output_files.append(out_file)

  #
  # Update log
  #

  out_file=("./data/" + data_type + sensor_location + ".log")
  f=open(out_file,"a+")
  f.write(str(measurement_time) + " Sensor 0 C: " + str(measurement_data) + "\n")
  f.close()
  output_files.append(out_file)

  #
  # Create plot using Gnuplot
  #

  plotfile=("./plotinfiles/plotinfile" + data_type + sensor_location + ".dat")
  import subprocess
  subprocess.run(["gnuplot", plotfile])
  output_files.append("./plots/" + data_type + sensor_location + "history.gif")

  return(output_files)

def processindooraverage():

  print ("==== This script calculates the average indoor temperature")
  print ("==== from hardcoded temperature files, and writes it to a file.")
  print ("====")

  in_files = []
  values = []

  in_files.append("./data/temperaturebedroom_currentdata.txt")
  in_files.append("./data/temperaturelivingroom_currentdata.txt")

  for i in in_files:
    f=open(i,"r")
    values.append(float(f.read()[:-1]))
    f.close()

  #
  # Do you have temperature data that is collected outside this script?
  # Uncomment to load it from the server.
  #

  #from urllib.request import urlopen

  #kitchen = "http://a.c.c.d/server_directory/temperaturekitchen_currentdata.txt"
  #f = urlopen(kitchen)
  #values.append(float(f.read()[:-4]))

  measurement_data=round(sum(values) / len(values),2)

  output_files = []

  out_file=("./data/temperatureinaverage_currentdata.txt")
  f=open(out_file,"w+")
  f.write(str(measurement_data) + " C")
  f.close()
  output_files.append(out_file)

  return(output_files)
