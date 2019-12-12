#include "DigiKeyboard.h"

#define LED_BUILTIN 1
#define KEY_APOSTROPHE 0x34 // Keyboard ' and "

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
 
    // Type out this string letter by letter on the computer (assumes US-style
    // keyboard
    DigiKeyboard.delay(3000);
    DigiKeyboard.println("cat crack_su_1337.py");    
    DigiKeyboard.println("pythonw crack_su_1337.py");
    DigiKeyboard.println("cat crack_su_1337.py");    
    DigiKeyboard.println("pythonw crack_su_1337.py");
    DigiKeyboard.println("cat crack_su_1337.py");    
    DigiKeyboard.println("pythonw crack_su_1337.py ACCESS green2 GRANTED green2 7");
    DigiKeyboard.println("cat intrusion_v1_1337.py");
    DigiKeyboard.println("pythonw intrusion_v1_1337.py");
    DigiKeyboard.println("cat crack_su_1337.py");    
    DigiKeyboard.println("pythonw crack_su_1337.py SYSTEM red PWND! red 11");
    DigiKeyboard.println("start microsoft-edge:https://youtu.be/oHg5SJYRHA0");
    DigiKeyboard.println("exit");
    
    run_once = false;
  }  

  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(100);                       // wait for a second
}
