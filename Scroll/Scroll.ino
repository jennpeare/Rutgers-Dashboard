

// include the library code:
#include <LiquidCrystal.h>
#include <Time.h>
#include <DateTime.h>
#include <DateTimeStrings.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); 
String blank = "                    ";
String s = "Hello world!";

void setup() {
  Serial.begin(9600);
  Serial.println("Waiting for time sync message");
  lcd.begin(20, 2);  // set up the LCD's number of columns and rows
  lcd.noCursor();
}

void loop() {
  scrollingText();
}

void scrollingText() {
  // scroll 13 positions (string length) to the left 
  // to move it offscreen left:
  String text;
  for (int i = 0; i < blank.length(); i++) {
    if (i >= s.length()) {
      text = blank.substring(i) + s;
    } else {
      text = blank.substring(i) + s.substring(0, i);
    }
    lcd.print(text);
    delay(200);
    lcd.clear();
    lcd.setCursor(0, 0);
  }
  
  for (int i = 0; i < s.length(); i++) {
    text = s.substring(i);
    lcd.print(text);
    delay(200);
    lcd.clear();
    lcd.setCursor(0, 0);
  }
}



