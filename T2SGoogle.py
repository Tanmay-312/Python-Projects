from gtts import gTTS
import os

# Enter the text
input_text = input("Enter the text: ")
# Setting the language
language = "en"
# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)
# Creating and saving the audio file
voice.save("Demo.mp3")
# playing the file
os.system("start Demo.mp3")
