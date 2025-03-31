#include <Arduino.h>

int TDS_pin = 6;
int thermal_pin = 5;
int level_pin = 11;
int level_pin_2 = 5;
int thermal_pin2 = 10;
int ph_pin = 9;

float tds = 0;
int farenheit = 0;
int farenheit2 = 0;
float water_level = 0;
float water_level_2 = 0;
float ph_level = 0;

void setup() {
  pinMode(TDS_pin, INPUT);
  pinMode(thermal_pin, INPUT);
  Serial.begin(9600);
}

int get_thermal_data() {
  int sensorValue = analogRead(thermal_pin); 

  float voltage = sensorValue * (5.0 / 1023.0);

  float celsius = (voltage - 0.5) * 100;

  float farenheit_val = (celsius * 9.0) / 5.0;

  farenheit_val -= 80;

  Serial.println("FAR" + String(farenheit));

  return farenheit_val;
}

float get_ph_level(){
  int sensorValue = analogRead(ph_pin); 

  float voltage = sensorValue * (5.0 / 1023.0);

  float ph_val = 5 - (voltage - 2.5);

  Serial.println("PHL" + String(ph_level));

  return ph_val;
}

float get_thermal_data_2(){
  int sensorValue = analogRead(thermal_pin); 

  float voltage = sensorValue * (5.0 / 1023.0);

  float celsius = (voltage - 0.5) * 100;

  float farenheit_val = (celsius * 9.0) / 5.0;

  farenheit_val -= 80;

  Serial.println("FA2" + String(farenheit2));

  return farenheit_val;
}

int get_tds_data() {
  int sensorValue = analogRead(TDS_pin); 

  float voltage = (float) sensorValue * (5.0 / 1023.0);

  float tds_val = (133.42 * voltage * voltage * voltage - 255.86 * voltage * voltage + 857.39 * voltage) * 0.5; 

  tds_val -= 150;

  Serial.println("TDS" + String(tds_val));

  return tds_val;
}

int get_water_level(){
  float water_level_val = analogRead(level_pin) * (1.625 / 1023);

  Serial.println("WLS" + String(water_level_val));

  return water_level_val;
}

int get_water_level_2(){
  float water_level_val_2 = analogRead(level_pin_2) * (1.625 / 1023);

  Serial.println("WL2" + String(water_level_val_2));

  return water_level_val_2;
}

void loop() {
  farenheit = get_thermal_data();

  water_level_2 = get_water_level_2();

  farenheit2 = get_thermal_data_2();

  ph_level = get_ph_level();

  tds = get_tds_data();

  water_level = get_water_level();

  delay(100); 
}
