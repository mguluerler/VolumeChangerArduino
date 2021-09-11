void setup() {
  Serial.begin(115200);
}

void loop() {
  static int zero_hun = 0;
  static int value = 0;
  static int value_mapped = 0;
  if (10 < abs(value - analogRead(A0))){ //For ignore noise
    value = analogRead(A0);
    value_mapped = map(1023-value, 0, 1023, 0, 100); //If you connect opposite, change the "1023-value" as "value"
    if (zero_hun != value_mapped){
      zero_hun = value_mapped;
      Serial.println(String(zero_hun));
    }
    delay(10);
  }
}
