#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

#include <OneWire.h>


ESP8266WiFiMulti WiFiMulti;

OneWire  ds(D2);  // on pin D4 (a 4.7K resistor is necessary)

float read_temp() {
    byte i;
    byte present = 0;
    byte type_s;
    byte data[12];
    byte addr[8];
    float celsius;

    ds.reset_search();

    if (!ds.search(addr)) {
        Serial.println("search fail");
        ds.reset_search();
        delay(250);
        return 85.0;
    }

    if (OneWire::crc8(addr, 7) != addr[7]) {
        Serial.println("CRC is not valid!");
        return 85.0;
    }
    Serial.println();

    // the first ROM byte indicates which chip
    switch (addr[0]) {
    case 0x10:
        type_s = 1;
        break;
    case 0x28:
        type_s = 0;
        break;
    case 0x22:
        type_s = 0;
        break;
    default:
        Serial.println("Device is not a DS18x20 family device.");
        return 85.0;
    }

    ds.reset();
    ds.select(addr);
    ds.write(0x44);  // start conversion, definitely not parasite
    delay(1000);
    present = ds.reset();
    ds.select(addr);
    ds.write(0xBE); // Read Scratchpad

    for ( i = 0; i < 9; i++) {
        data[i] = ds.read();
    }

    // Convert the data to actual temperature
    int16_t raw = (data[1] << 8) | data[0];
    if (type_s) {
        raw = raw << 3; // 9 bit resolution default
        if (data[7] == 0x10) {
            raw = (raw & 0xFFF0) + 12 - data[6];
        }
    } else {
        byte cfg = (data[4] & 0x60);
        if (cfg == 0x00) raw = raw & ~7;  // 9 bit resolution, 93.75 ms
        else if (cfg == 0x20) raw = raw & ~3; // 10 bit res, 187.5 ms
        else if (cfg == 0x40) raw = raw & ~1; // 11 bit res, 375 ms
    }
    celsius = (float)raw / 16.0;
    Serial.print("  Temperature = ");
    Serial.print(celsius);
    Serial.print(" Celsius, ");
    Serial.println(":");
    return celsius;
}


void setup() {
    Serial.begin(9600);

    delay(4000);

    WiFiMulti.addAP("SSID", "passwd");
}


void loop() {
    boolean ok = false;

    if (WiFiMulti.run() == WL_CONNECTED) {
        float temp = read_temp();

        if (temp < 85.00) {
            HTTPClient http;

            http.begin("http://a.b.c.d:8086/write?db=temperature");

            String postContent = "temp,dev=d3 value=" + String(temp, 2);

            int httpCode = http.POST(postContent);

            http.end();

        }

        ok = true;
    }

    if (ok) {
        // enter deep sleep
        int sleepSeconds = 1800;
        ESP.deepSleep(sleepSeconds * 1000000);
    } else {
        delay(10000);
    }
}
