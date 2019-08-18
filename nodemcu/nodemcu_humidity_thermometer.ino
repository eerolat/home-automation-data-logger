#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

#include <WEMOS_SHT3X.h>

SHT3X sht30(0x45);


ESP8266WiFiMulti WiFiMulti;


float read_temp() {
    float celsius;

    if(sht30.get()==0){
        celsius = (float)sht30.cTemp;
        
        Serial.print("  Temperature = ");
        Serial.println(celsius);
        Serial.print(" Celsius ");
        Serial.println();
        }
    else {
       Serial.println("Error!");
       delay(1000);
       return 85.0;
       }
    
    return celsius;
}


float read_humid() {
    float humid;

    if(sht30.get()==0){
        humid = (float)sht30.humidity;
        
        Serial.print("  Relative Humidity = ");
        Serial.println(humid);
        Serial.println();
        }
    else {
       Serial.println("Error!");
       delay(1000);
       return 100.01;
       }
    
    return humid;
}


void setup() {
    Serial.begin(115200);

    delay(4000);

    WiFiMulti.addAP("SSID", "passwd");
}


void loop() {
    boolean ok = false;

    if (WiFiMulti.run() == WL_CONNECTED) {
        float temp = read_temp();
        delay(1000);
        float humid = read_humid();

        if (temp < 85.00) {
            HTTPClient http;

            http.begin("http://a.b.c.d:8086/write?db=temperature");

            String postContent = "temp,dev=d4 value=" + String(temp, 2);

            int httpCode = http.POST(postContent);

            // nah, I don't care

            http.end();

        }

        delay(250);

        if (humid < 100.01) {
            HTTPClient http;

            http.begin("http://a.b.c.d:8086/write?db=humidity");

            String postContent = "humid,dev=d4 value=" + String(humid, 2);

            int httpCode = http.POST(postContent);

            // nah, I don't care

            http.end();

        }

        ok = true;
    }

    if (ok) {
        //enter deep sleep
        int sleepSeconds = 1800;
        ESP.deepSleep(sleepSeconds * 1000000);
    } else {
        delay(10000);
    }
}
