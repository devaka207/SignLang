import RPi_I2C_driver


import RPi.GPIO as GPIO


import time

#import tim


mylcd = RPi_I2C_driver.lcd()


mylcd.backlight(1)


mylcd.lcd_clear()


time.sleep(1)


L1 = 16


L2 = 20


L3 = 21


L4 = 5


C1 = 6


C2 = 13


C3 = 19


C4 = 2


GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)


GPIO.setup(L1, GPIO.OUT)


GPIO.setup(L2, GPIO.OUT)


GPIO.setup(L3, GPIO.OUT)


GPIO.setup(L4, GPIO.OUT)


GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readLine(line, characters):


    GPIO.output(line, GPIO.HIGH)


    if(GPIO.input(C1) == 1):


        print(characters[0])


        mylcd.lcd_write_char(ord(characters[0]))


    if(GPIO.input(C2) == 1):


        print(characters[1])


        mylcd.lcd_write_char(ord(characters[1]))


    if(GPIO.input(C3) == 1):


        print(characters[2])


        mylcd.lcd_write_char(ord(characters[2]))


    if(GPIO.input(C4) == 1):


        print(characters[3])


        mylcd.lcd_write_char(ord(characters[3]))


    GPIO.output(line, GPIO.LOW)


try:


    while True:


        readLine(L1, ["1","2","3","A"])


        readLine(L2, ["4","5","6","B"])


        readLine(L3, ["7","8","9","C"])


        readLine(L4, ["*","0","#","D"])


        time.sleep(0.3)


except KeyboardInterrupt:


    print("\nProgram is stopped")

