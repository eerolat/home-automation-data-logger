# Tuomas Eerola - 2019
# Python3 script
# requires sys, csv

import sys
import csv

print ("==== This script reads sensor list from a csv file")
print ("==== File format: sensor_id,sensor_location,sensor_data_type")

def readsensorlist(csvfile):
  with open(csvfile, 'r') as f:
    reader=csv.reader(f)
    sensors=list(reader)

  return sensors
