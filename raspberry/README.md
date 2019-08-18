# Raspberry Pi script

These scripts runs on your Raspberry Pi and publish your data on a web server.

- read_ds18b20.sh - Reads a local ds18b20 one-wire sensor connected to your Raspberry Pi
- read_influx.sh - Reads sensor data from your InfluxDB

## Getting Started

Use cron to schedule these scripts.

The scripts use:

- jq https://stedolan.github.io/jq/
- digitemp_DS9097 https://www.digitemp.com/
- gnuplot http://www.gnuplot.info/

## Authors

* **Tuomas Eerola** - *Initial work* - [GitHub](https://github.com/eerolat)
