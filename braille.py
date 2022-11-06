import speech_recognition as sr
import numpy as np
import os
from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import PIL
import pyttsx3
from pygame import mixer
from gtts import gTTS
from playsound import playsound
try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract
import cv2
from picamera import PiCamera
import time
import pyttsx3
from translate import Translator

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

##def speechToText():
##    rec = sr.Recognizer()
##    mic = sr.Microphone()
##    with mic as source:
##        rec.adjust_for_ambient_noise(source)
##        audio = rec.listen(source)
##        return(str(rec.recognize_wit(audio, wit_api_key)))

def textToBraille(text):
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
    print(final_string)

##def speechToBraille():
##    textToBraille(speechToText())

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
#new file
#new file

##engine = pyttsx3.init()
##camera = PiCamera()
##camera.start_preview()
##time.sleep(2)
##camera.capture('image2.png')
##camera.stop_preview()
##time.sleep(2)
##camera.close()
##
##image = cv2.imread('text.png')
##
##gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
##thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
##thresh = cv2.GaussianBlur(thresh, (3,3), 0)
### cv2.imshow('Window', thresh)
### cv2.waitKey()
### cv2.destroyAllWindows()
##data = pytesseract.image_to_string(gray, config=' ')
##print(data)
##objTrans=clsTranslate()
##strTranslatedText= objTrans.translateText(data, 'kn')
##print(strTranslatedText)
##myobj = gTTS(text=strTranslatedText, lang=language, slow=False)
##myobj.save("welcome.mp3")
##mixer.music.load("welcome.mp3")
##mixer.music.play()
##time.sleep(2)
##voices = engine.getProperty('voices')
##engine.setProperty('voice', voices[0].id) 
##engine.setProperty('rate', 100)
##engine.setProperty('volume', 12.0) 
##engine.say(strTranslatedText)
##
##engine.runAndWait()
##textToBraille("czx")
##textToBraille(data)


