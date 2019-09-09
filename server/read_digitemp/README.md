# 1-wire sensor data to InfluxDB

This Python scripts runs on your server (Raspberry Pi or similar), reads a locally connected 1-wire sensor, and writes the data to your InfluxDB.

## Getting Started

Edit:

- Install and configure your Digitemp.
- The script assumes InfluxDB databases called "temperature". If your database has a different names update the script.

Use cron to schedule the script:

- read_digitemp.py

The script uses:

- digitemp_DS9097 https://www.digitemp.com/

## Authors

* **Tuomas Eerola** - *Initial work* - [GitHub](https://github.com/eerolat)
