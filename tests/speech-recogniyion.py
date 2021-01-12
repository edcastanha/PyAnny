import speech_recognition as sr


#Cria reconhecedor
r = sr.Recognizer()


# abrir microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)

        print(r.recognize_google(audio))