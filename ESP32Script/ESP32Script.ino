#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "Name of WiFi network";
const char *password = "WiFi password";
const char *flaskServerUrl = "http://localhost:5000/finger_count"; 

const int ledPin1 = 13; 
const int ledPin2 = 12;
const int ledPin3 = 14; 
const int ledPin4 = 33; 
const int ledPin5 = 25;

void setup() {
    Serial.begin(115200);

    
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
    pinMode(ledPin3, OUTPUT);
    pinMode(ledPin4, OUTPUT);
    pinMode(ledPin5,OUTPUT);

    digitalWrite(ledPin1, LOW); 
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
    digitalWrite(ledPin4, LOW);
    digitalWrite(ledPin4,LOW);

    delay(5000); 
}

void loop() {
    
    int fingerCount = getFingerCount();
    turnOnLEDs(fingerCount);
    delay(100);
}

void turnOnLEDs(int count) {
    digitalWrite(ledPin1, count >= 1 ? HIGH : LOW);
    digitalWrite(ledPin2, count >= 2 ? HIGH : LOW);
    digitalWrite(ledPin3, count >= 3 ? HIGH : LOW);
    digitalWrite(ledPin4, count >= 4 ? HIGH : LOW);
    digitalWrite(ledPin5, count >= 5 ? HIGH : LOW);
}

int getFingerCount() {
    HTTPClient http;
    http.begin(flaskServerUrl);

    int httpResponseCode = http.GET();
    int fingerCount = 0;

    if (httpResponseCode == HTTP_CODE_OK) {
        
        String payload = http.getString();
        fingerCount = payload.substring(payload.indexOf(":") + 1).toInt();
    } else {
        Serial.printf("HTTP Request failed: %s\n", http.errorToString(httpResponseCode).c_str());
    }

    http.end();
    return fingerCount;
}

