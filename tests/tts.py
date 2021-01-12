import pyttsx3

engine = pyttsx3.init()


voices = engine .getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say("Vou falar desta forma até a Caroline olhar para o lado")
engine.runAndWait()