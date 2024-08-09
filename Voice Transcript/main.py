import assemblyai as aai

aai.settings.api_key = "3fa33c0dbb9f4b5591fb849343a9e5f6" 

transcriber = aai.Transcriber()

audio_url = "Keep Your Joints Healthy With These Simple Tips - Top Health Coach Luke Coutinho.mp3"

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_url, config)

if transcript.error:
   print(transcript.error)

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")

# For accessing this, money is required
prompt = input("Ask a question based on transcript.")

result = transcript.lemur.task(prompt)

print(result.response)

