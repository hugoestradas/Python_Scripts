import os
import assemblyai as aai
from pytube import YouTube

aai.settings.api_key = "Aquí va la llave de tu API"
youtube_url = "https://www.youtube.com/watch?v=S4uYd90Zplw"

# primero descargamos el video de youtube
youtube = YouTube(youtube_url)
audio = youtube.streams.filter(only_audio =  True).first()
filename = os.path.basename(audio.download())

# procedemos a transcribir el video
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(filename)
print(transcript.text)

# en esta parte hacemos el resumen del video
summary = transcript.lemur.summarize(
    context = "A great tech event is coming in Guatemala"
    )
print(summary.response)

# y ahora podemos preguntar cosas específicas sobre el video
questions =[
    aai.LemurQuestion(question="When is the upcoming event?"),
    aai.LemurQuestion(question="Who is organizing the event?"),
    aai.LemurQuestion(question="Is it going to be a free event?")
    ]
    
answers = transcript.lemur.question(questions)

for answer in answers.response:
    print(f"Question: "{answer.question}"")
    print(f"Answer: "{answer.answer}"")
