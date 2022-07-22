import speech_recognition as sr
r = sr.Recognizer()
print("please talk")
with sr.Microphone() as source :
    audio_data = r.record(source,duration=5)
    print("recognizing")
    text = r.recognize_google(audio_data)
    print(text)