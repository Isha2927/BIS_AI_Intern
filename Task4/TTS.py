from gtts import gTTS

text = """
Hello everyone.
Welcome to the Speech-to-Text demonstration.
"""

tts = gTTS(text=text, lang='en')

tts.save("output.mp3")

print("Audio saved successfully!")