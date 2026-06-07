import speech_recognition as sr

print("=" * 50)
print("VOICE2TEXT AI TRANSCRIBER")
print("=" * 50)

recognizer = sr.Recognizer()

audio_file = "sample.wav"

with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)

    print("\nTranscribed Text:\n")
    print(text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("Internet connection error")