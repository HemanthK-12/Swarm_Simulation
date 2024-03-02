void setup() {
    Serial.begin(9600);
     pinMode(6, OUTPUT);
    pinMode(5, OUTPUT);

}

void loop() {
    digitalWrite(6,HIGH);
    digitalWrite(5,HIGH);
    delay(500); // set delay time
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    delay(500); // set delay time
}