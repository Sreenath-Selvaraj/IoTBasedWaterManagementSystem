#include <ESP8266WiFi.h>
int low=D1;
int high=D2,l,h;
const char* ssid = "Sree";
const char* password = "9043935058";
WiFiServer server(80);
void setup() {
  Serial.begin(115200);
  delay(10);
 
  pinMode(low, INPUT);
  pinMode(high, INPUT);
  l=digitalRead(low);

  h=digitalRead(high);
 
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 

  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
  }
 void loop() {
  l=digitalRead(low);
  h=digitalRead(high);
  // Check if a client has connected
  WiFiClient client = server.available();
  String req = client.readStringUntil('\r');
  client.flush();
  Serial.println(l);
  Serial.println(h);
  String s = "HTTP/1.1 200 OK\r\n";
  s += "Content-Type: text/html\r\n\r\n";
  s += "<!DOCTYPE HTML>\r\n<html>";
   if(l==1 && h==1)
   {
  s +="2";

   }
    
 else if(l==1 && h==0)
 { 
    s +="1";
 }
  else
  { 
    s +="0";
  }
  s += "</html>";
 client.print(s);
 }
