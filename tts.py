from gtts import gTTS  
from playsound import playsound  
text_val = 'vishnu suresh perumbavoor will destroy the planet. artificial intelligence and blockchain is the future'  
language = 'en'  
obj = gTTS(text=text_val, lang=language, slow=False)  
obj.save("exam.mp3")  
playsound("exam.mp3")  