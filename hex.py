import RPi.GPIO as GPIO
import time
from gtts import gTTS
from pygame import mixer
import lcddriver
lcd = lcddriver.lcd()

language = 'en'
mixer.init()

L1 = 16
L2 = 20
L3 = 21
L4 = 5

C1 = 6
C2 = 13
C3 = 19
C4 = 26

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
        #print(characters[0])
        mytxt=characters[0]
        print(mytxt)
        lcd.lcd_display_string(mytxt, 1)
        myobj = gTTS(text=mytxt, lang=language, slow=False)
        myobj.save("A.mp3")
        mixer.music.load("A.mp3")
        mixer.music.play()
        time.sleep(3)
    if(GPIO.input(C2) == 1):
        #print(characters[1])
        mytxt=characters[1]
        print(mytxt)
        lcd.lcd_display_string(mytxt, 1)
        myobj = gTTS(text=mytxt, lang=language, slow=False)
        myobj.save("A.mp3")
        mixer.music.load("A.mp3")
        mixer.music.play()
        time.sleep(3)
    if(GPIO.input(C3) == 1):
        #print(characters[2])
        mytxt=characters[2]
        print(mytxt)
        lcd.lcd_display_string(mytxt, 1)
        myobj = gTTS(text=mytxt, lang=language, slow=False)
        myobj.save("A.mp3")
        mixer.music.load("A.mp3")
        mixer.music.play()
        time.sleep(3)
    if(GPIO.input(C4) == 1):
        #print(characters[3])
        mytxt=characters[3]
        print(mytxt)
        lcd.lcd_display_string(mytxt, 1)
        myobj = gTTS(text=mytxt, lang=language, slow=False)
        myobj.save("A.mp3")
        mixer.music.load("A.mp3")
        mixer.music.play()
        time.sleep(0.1)
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(L1, ["Hi","Hello","How are you","Iam Fine"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["E","F","G","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
    lcd.lcd_display_string("Application stopped!", 1)