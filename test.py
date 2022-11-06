import mediapipe as mp
import cv2
import numpy as np
import lcddriver
from time import *
lcd = lcddriver.lcd()

from data_collection import draw_landmarks, extract_keypoints, mediapipe_detection

from model import create_model
from gtts import gTTS
import speech_recognition as sr
import os
from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import pyttsx3
from pygame import mixer
try:
    from PIL import Image
except ImportError:
    import Image

from picamera import PiCamera
from translate import Translator

language = 'en'
mixer.init()

mp_holistic=mp.solutions.holistic
mp_drawing=mp.solutions.drawing_utils

sequence=[]
sentence=[]
thresh=0.8
actions=[]
for ie in range(97,123):
    actions.append(chr(ie))
lcd.lcd_display_string(" Sign language", 1)
lcd.lcd_display_string("  detection   ", 2)
cap=cv2.VideoCapture(0)

model=create_model()
model.load_weights('action3.h5')
res=np.array([2.9485551e-20,8.7930697e-18,4.4212179e-16,3.8555774e-24,4.7811854e-32
,3.9088125e-11,6.2194567e-37,4.1775081e-21,1.1696461e-07,9.9999988e-01
,4.5697821e-24,2.0483630e-15,5.7101654e-12,4.6459605e-17,2.9196457e-08
,8.6699751e-23,1.4897640e-13,2.7513793e-18,2.8300720e-15,1.8070643e-18
,1.9550273e-19,4.8556037e-26,2.5306402e-19,3.2431286e-26,2.4559270e-11
,1.7702510e-22])

class clsTranslate():

    def translateText(self, strString, strTolang):
        self.strString = strString
        self.strTolang = strTolang
        translator = Translator(to_lang=self.strTolang)
        translation = translator.translate(self.strString)
        return (str(translation))

language = 'en'
mixer.init()


global void
global a
global b
global c
global d
global e
global f
global g
global h
global i
global j
global k
global l
global m
global n
global o
global p
global q
global r
global s
global t
global u
global v
global w
global x
global y
global z

charToArray = {
    " " : [[0,0],[0,0],[0,0]],
    "a" : [[1,0],[0,0],[0,0]],
    "b" : [[1,0],[1,0],[0,0]],
    "c" : [[1,1],[0,0],[0,0]],
    "d" : [[1,1],[0,1],[0,0]],
    "e" : [[1,0],[0,1],[1,0]],
    "f" : [[1,1],[1,0],[0,0]],
    "g" : [[1,1],[1,1],[0,0]],
    "h" : [[1,0],[1,1],[0,0]],
    "i" : [[0,1],[1,0],[1,0]],
    "j" : [[0,1],[1,1],[0,0]],
    "k" : [[1,0],[0,0],[1,0]],
    "l" : [[1,0],[1,0],[1,0]],
    "m" : [[1,1],[0,0],[1,0]],
    "n" : [[1,1],[0,1],[1,0]],
    "o" : [[1,0],[0,1],[1,1]],
    "p" : [[1,1],[1,0],[1,0]],
    "q" : [[1,1],[1,1],[1,0]],
    "r" : [[1,0],[1,1],[1,0]],
    "s" : [[0,1],[1,0],[1,0]],
    "t" : [[0,1],[1,1],[1,0]],
    "u" : [[1,0],[0,0],[1,1]],
    "v" : [[1,0],[1,0],[1,1]],
    "w" : [[0,1],[0,1],[1,1]],
    "x" : [[1,1],[0,0],[1,1]],
    "y" : [[1,1],[0,1],[1,1]],
    "z" : [[1,0],[0,1],[1,1]],
    "1" : [[1,0],[1,1],[1,1]]
}

ascii_braille = {}

asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
          '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
          '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

arrayLength = len(asciicodes)
counter = 0

while counter < arrayLength:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

letterToImgPath = {
    "a": "/Users/aadittrivedi/Desktop/braille/a.png",
    "b": "/Users/aadittrivedi/Desktop/braille/b.png",
    "c": "/Users/aadittrivedi/Desktop/braille/c.png",
    "d": "/Users/aadittrivedi/Desktop/braille/d.png",
    "e": "/Users/aadittrivedi/Desktop/braille/e.png",
    "f": "/Users/aadittrivedi/Desktop/braille/f.png",
    "g": "/Users/aadittrivedi/Desktop/braille/g.png",
    "h": "/Users/aadittrivedi/Desktop/braille/h.png",
    "i": "/Users/aadittrivedi/Desktop/braille/i.png",
    "j": "/Users/aadittrivedi/Desktop/braille/j.png",
    "k": "/Users/aadittrivedi/Desktop/braille/k.png",
    "l": "/Users/aadittrivedi/Desktop/braille/l.png",
    "m": "/Users/aadittrivedi/Desktop/braille/m.png",
    "n": "/Users/aadittrivedi/Desktop/braille/n.png",
    "o": "/Users/aadittrivedi/Desktop/braille/o.png",
    "p": "/Users/aadittrivedi/Desktop/braille/p.png",
    "q": "/Users/aadittrivedi/Desktop/braille/q.png",
    "r": "/Users/aadittrivedi/Desktop/braille/r.png",
    "s": "/Users/aadittrivedi/Desktop/braille/s.png",
    "t": "/Users/aadittrivedi/Desktop/braille/t.png",
    "u": "/Users/aadittrivedi/Desktop/braille/u.png",
    "v": "/Users/aadittrivedi/Desktop/braille/v.png",
    "w": "/Users/aadittrivedi/Desktop/braille/w.png",
    "x": "/Users/aadittrivedi/Desktop/braille/x.png",
    "y": "/Users/aadittrivedi/Desktop/braille/y.png",
    "z": "/Users/aadittrivedi/Desktop/braille/z.png",
    " ": "/Users/aadittrivedi/Desktop/braille/void.png",
}

def addImages(list_im):
    imgs = [ PIL.Image.open(i) for i in list_im ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save('output.jpg')  
 
def writeImage(b_string):
    images = []
    for letter in b_string:
        images.append(letterToImgPath[letter])
    addImages(images)    
    img = Image.open('output.jpg')
    img.show()

def writeText(b_string):
    final_string = ''
    for letters in b_string:
        final_string = final_string + ascii_braille[letters.lower()]
    print(final_string)

def speechToText():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
      rec.adjust_for_ambient_noise(source)
    audio = rec.listen(source)
    return(str(rec.recognize_wit(audio, wit_api_key)))

def textToBraille(text):
    global final_string
    final_string = ''
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["a"]))
        elif char == "b":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["b"]))
        elif char == "c":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["c"]))
        elif char == "d":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["d"]))
        elif char == "e": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["e"]))
        elif char == "f": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["f"]))
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
##            print(char + " " + str(charToArray["g"]))
        elif char == "h": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["h"]))
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
##            print(char + " " + str(charToArray["i"]))
        elif char == "j": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["j"]))
        elif char == "k": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["k"]))
        elif char == "l": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["l"]))
        elif char == "m": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["m"]))
        elif char == "n": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["n"]))
        elif char == "o":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["o"]))
        elif char == "p": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["p"]))
        elif char == "q": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["q"]))
        elif char == "r": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["r"]))
        elif char == "s": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["s"]))
        elif char == "t": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["t"]))
        elif char == "u": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["u"]))
        elif char == "v": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["v"]))
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
##            print(char + " " + str(charToArray["w"]))
        elif char == "x": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["x"]))
        elif char == "y": 
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["y"]))
        elif char == "z":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["z"]))
        elif char == "1":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray["1"]))
        elif char == " ":
            final_string = final_string + ascii_braille[char]
##            print(char + " " + str(charToArray[" "]))
##    print(final_string)
 
##def speechToBraille():
##    textToBraille(speechToText())
engine = pyttsx3.init()
def textToSpeech(text):
    os.system("espeak '" + str(text) + "'")

def brailleToTextArray(array):
    new_chars = ''
    for key in array:
        for a_key in charToArray:
            if charToArray[a_key] == key:
                new_chars = new_chars + str(a_key)
    return new_chars

def brailleToSpeechArray(array):
    textToSpeech(brailleToTextArray(array))

def brailleToSpeechImg(imgs):
    for img in imgs:
        for chars in letterToImgPath:
            if img == letterToImgPath[chars]:
                print(chars)

def imageToText(img):
    return image_to_string(Image.open(img))

def imageToSpeech(img):
    textToSpeech(imageToText(img))

def imageToBraille(img):
    textToBraille(imageToText(img))
lcd.lcd_display_string("              ", 1)
lcd.lcd_display_string("              ", 2)
while True:
    # speechToText()

 with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret,frame=cap.read()

        image,results=mediapipe_detection(frame,holistic)

        draw_landmarks(image,results)

        keypoints=extract_keypoints(results)
        sequence.insert(0,keypoints)
        sequence=sequence[:10]
        #print(keypoints)
        if len(sequence)==10:
            res=model.predict(np.expand_dims(sequence,axis=0))[0]
            print(actions[np.argmax(res)])
            tt=actions[np.argmax(res)]
            textToBraille(actions[np.argmax(res)])
            print(final_string)
            lcd.lcd_display_string("Sign  Detected:", 1)
            lcd.lcd_display_string(str(actions[np.argmax(res)]), 2)
##            textToSpeech(tt)
            if tt=='o':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("Hello", 1)
                mytext="Hello"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("Hello.mp3")
                mixer.music.load("Hello.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='c':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("How are you?", 1)
                mytext="How are you"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("How are you?.mp3")
                mixer.music.load("How are you?.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='i':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("Welcome", 1)
                mytext="Welcome"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                mixer.music.load("welcome.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='v':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("I'm fine", 1)
                mytext="I'm fine"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("I'm fine.mp3")
                mixer.music.load("I'm fine.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='x':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("What are you doing?", 1)
                mytext="What are you doing?"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("What are you doing?.mp3")
                mixer.music.load("What are you doing?.mp3")
                mixer.music.play()
                sleep(10)
            if tt=='a':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("What is your name?", 1)
                mytext="What is your name?"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("What is your name?.mp3")
                mixer.music.load("What is your name?.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='f':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("How is the work going on", 1)
                mytext="How is the work going on"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("How is the work going on.mp3")
                mixer.music.load("How is the work going on.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='m':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("Excuse me", 1)
                mytext="Excuse me"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("Excuse me.mp3")
                mixer.music.load("Excuse me.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='w':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("Thank you so much", 1)
                mytext="Thank you so much"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("Thank you so much.mp3")
                mixer.music.load("Thank you so much.mp3")
                mixer.music.play()
                sleep(1)
            if tt=='y':
                lcd.lcd_display_string("                ", 1)
                lcd.lcd_display_string("How was you day?", 1)
                mytext="How was you day?"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("How was you day?.mp3")
                mixer.music.load("How was you day?.mp3")
                mixer.music.play()
                sleep(1)
##            voices = engine.getProperty('voices')
##            engine.setProperty('voice', voices[0].id) 
##            engine.setProperty('rate', 100)
##            engine.setProperty('volume', 12.0) 
##            engine.say(str(tt))
##            ##
##            engine.runAndWait()
        else:
            continue
##        print(res[np.argmax(res)])
        if res[np.argmax(res)]>thresh:
            if(len(sentence) > 0):
                if actions[np.argmax(res)]!=sentence[-1]:
                    sentence.append(actions[np.argmax(res)])
            else:
                sentence.append(actions[np.argmax(res)])

        if(len(sentence)>5):
            sentence=sentence[-5:]

        cv2.rectangle(image,(0,0),(640,40),(27,114,245),-1)
        cv2.putText(image,' '.join(sentence),(3,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
        

        cv2.imshow('Sign Lang',image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
