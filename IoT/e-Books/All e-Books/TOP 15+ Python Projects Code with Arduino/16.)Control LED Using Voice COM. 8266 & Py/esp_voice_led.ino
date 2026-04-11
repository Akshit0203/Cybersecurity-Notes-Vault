#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "subrata wi-fi"; // Replace with your Wifi ssid
const char* password = "Subrat@007"; // Replace with your WiFi password

ESP8266WebServer server(80);
int ledPin = D1;

void handleRoot() {
  String message = "LED Control\n";
  message += "Send /on or /off to control the LED\n";
  server.send(200, "text/plain", message);
}

void handleLEDOn() {
  digitalWrite(ledPin, HIGH);
  server.send(200, "text/plain", "LED is ON");
}

void handleLEDOff() {
  digitalWrite(ledPin, LOW);
  server.send(200, "text/plain", "LED is OFF");
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up web server routes
  server.on("/", handleRoot);
  server.on("/on", handleLEDOn);
  server.on("/off", handleLEDOff);

  // Start the server
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}