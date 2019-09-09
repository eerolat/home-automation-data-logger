# Raspberry Pi script

These Python scripts run on your server (Raspberry Pi or similar) and publish the data on a web server.

- collect_sensor_data - Reads sensor data from your local InfluxDB, visualizes it using Gnuplot, creates text files that can be used on a web server (not included in this respository), and uploads the files to the web server.
- read_digitemp - Uses Digitemp to read temperature sensor data from a local ds18b20 1-wire sensor and pushes it into your InfluxDB

## Getting Started

Edit:

- Use sensorlist_template.csv to create a sensorlist.csv that matches your sensors.
- Use server_template.conf to create a server.conf that contains your web server details.
- Use the templates in plotinfiles directory to specify how you want your data to be visualized.
- Uncomment/ upadate the relevant processindooraverage lines in of collect_sensor_data.py
- The scripts assume InfluxDB databases called "temperature" and "humidity". If your databases have different names, update these.

Use cron to schedule the scripts:

- collect_sensor_data/collectsensors.py
- read_digitemp/read_digitemp.py

The scripts use:

- digitemp_DS9097 https://www.digitemp.com/
- gnuplot http://www.gnuplot.info/

## File locations

- collect_sensor_data/data - Logs and text files that can be used on a web server.
- collect_sensor_data/plots - Visualized data.
- collect_sensor_data/plotinfiles - Gnuplot files that specify the looks of the visualizations.

## Authors

* **Tuomas Eerola** - *Initial work* - [GitHub](https://github.com/eerolat)
