import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Test Succesful", 1)
lcd.lcd_display_string("A           ", 2)
lcd.lcd_display_string("picorder", 3)
lcd.lcd_display_string("I am a Raspberry Pi", 4)
