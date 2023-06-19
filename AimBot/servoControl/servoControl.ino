#include <Servo.h>
#include <Firmata.h>

#define SERVO_PIN_X 9
#define SERVO_PIN_Y 10

Servo servoX;
Servo servoY;

void setup() {
  Firmata.setFirmwareVersion(0, 1);
  Firmata.attach(ANALOG_MESSAGE, analogWriteCallback);
  Firmata.begin(57600);

  servoX.attach(SERVO_PIN_X);
  servoY.attach(SERVO_PIN_Y);
  servoX
}

void loop() {
  while (Firmata.available()) {
    Firmata.processInput();
  }
}

void analogWriteCallback(byte pin, int value) {
  if (pin == SERVO_PIN_X) {
    servoX.write(value);
  }
  else if (pin == SERVO_PIN_Y) {
    servoY.write(value);
  }
}