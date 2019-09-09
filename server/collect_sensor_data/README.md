# Visualize and publish IoT data

This Python script runs on your server (Raspberry Pi or similar), reads data from your InfluxDB, visualizes it, and publishes on your server.

## Getting Started

Edit:

- Use sensorlist_template.csv to create a sensorlist.csv that matches your sensors.
- Use server_template.conf to create a server.conf that contains your web server details.
- Use the templates in plotinfiles directory to specify how you want your data to be visualized.
- Uncomment/ upadate the relevant processindooraverage lines in of collect_sensor_data.py
- The script assumes InfluxDB databases called "temperature" and "humidity". If your databases have different names, update these.

Use cron to schedule the script:

- collectsensors.py

The script uses:

- gnuplot http://www.gnuplot.info/

## File locations

- collect_sensor_data/data - Logs and text files that can be used on a web server.
- collect_sensor_data/plots - Visualized data.
- collect_sensor_data/plotinfiles - Gnuplot files that specify the looks of the visualizations.

## Authors

* **Tuomas Eerola** - *Initial work* - [GitHub](https://github.com/eerolat)
