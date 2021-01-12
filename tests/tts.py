import pyttsx3

engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[53].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)

engine.say("Vou falar deste texto")
   

engine.runAndWait()