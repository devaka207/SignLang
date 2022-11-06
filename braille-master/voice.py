from gtts import gTTS
from pygame import mixer
import time
language = 'en'
mixer.init()
mytext="Moisture detected"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
mixer.music.load("welcome.mp3")
mixer.music.play()
time.sleep(2)
