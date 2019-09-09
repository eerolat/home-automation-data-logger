# Tuomas Eerola - 2019
# Python3 script
# requires sys, influxdb, datetime

import sys
from influxdb import InfluxDBClient
from datetime import datetime


def readinfluxdata(database, sensor_id):

  print ("==== This script reads sensor " + sensor_id + " data from a local InfluxDB")
  print ("==== and creates a plot that visualizes it.")
  print ("====")


  if (database == '-h'):
    print ("==== Database: Humidity")
    data_type="humidity"
    client=InfluxDBClient(host='localhost', port=8086, database='humidity')
  elif (database == '-t'):
    print ("==== Database: Temperature")
    data_type="temperature"
    client=InfluxDBClient(host='localhost', port=8086, database='temperature')
  else:
    print("Unknown database.")
    sys.exit()

  print ("==== Sensor ID: " + sensor_id)
  print ("")

  # read new data from influx

  if (database == '-h'):
    query = ("SELECT * from humid WHERE dev='" + sensor_id + "' GROUP by * ORDER by DESC LIMIT 1")
  else:
    query = ("SELECT * from temp WHERE dev='" + sensor_id + "' GROUP by * ORDER by DESC LIMIT 1")

  results = client.query(query,epoch='s') 

  points = results.get_points()

  for item in points:
    measurement_data = item['value']
    measurement_timestamp = item['time']
    measurement_time = datetime.fromtimestamp(measurement_timestamp)

  influxdata=[measurement_data,measurement_timestamp]

  return influxdata
