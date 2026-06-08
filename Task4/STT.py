import whisper

# Load Whisper model
# Options: tiny, base, small, medium, large
model = whisper.load_model("base")

# Audio file path
audio_file = "audio.mp3"   # Replace with your audio file

print("Transcribing audio...")

# Transcribe audio
result = model.transcribe(audio_file)

# Print full transcript
print("\n===== TRANSCRIPT =====\n")
print(result["text"])

# Save transcript
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write("FULL TRANSCRIPT\n\n")
    f.write(result["text"])

print("\nTranscript saved as transcript.txt")

# Print timestamps
print("\n===== TIMESTAMPS =====\n")

for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    text = segment["text"]

    print(f"[{start:.2f}s - {end:.2f}s] {text}")

# Save timestamps
with open("timestamps.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]

        f.write(f"[{start:.2f}s - {end:.2f}s] {text}\n")

print("\nTimestamps saved as timestamps.txt")