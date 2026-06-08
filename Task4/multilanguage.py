import whisper

model = whisper.load_model("base")

result = model.transcribe("marathiaudio.mp3")

print("Detected Language:", result["language"])
print("Transcript:")
print(result["text"])