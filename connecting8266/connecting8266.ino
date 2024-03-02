#include "ESP8266WiFi.h"
 
void setup(){
  Serial.begin(115200);
  WiFi.mode(WIFI_AP_STA);
  Serial.println(WiFi.macAddress());
}
 
void loop(){

}
