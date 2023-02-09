from gtts import gTTS
import os

text = "Hello, this is a text to speech conversion example using Python"

# Convert text to speech
tts = gTTS(text, lang='en')

# Save the speech to a file
tts.save("hello.mp3")

# Play the speech file
os.system("mpg321 hello.mp3")
