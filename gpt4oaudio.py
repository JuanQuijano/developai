import base64 
import os 
from openai import AzureOpenAI 

endpoint = "https://azureopeaitrainer.openai.azure.com/"
api_key="b4c4fd358ba94e75af1fa5bfe0dd476d"
api_version="2025-01-01-preview"
deployment = "gpt-4o-realtime-preview"

endpoint = "https://jcqu-m6jsngyu-eastus2.cognitiveservices.azure.com/"
api_key="6GcIQkWfuXx6B5ydmnuNATA9yC9vroBHp2YFCnuOM5pQOBJQCeDOJQQJ99BAACHYHv6XJ3w3AAAAACOGmm0r"
api_version="2025-01-01-preview"
deployment = "gpt-4o-realtime-preview"

client = AzureOpenAI(
    api_version=api_version,  
    api_key=api_key,
    azure_endpoint=endpoint
)


completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "¿Qué es mejor, un perro o un gato?"
        }
    ]
)

print(completion.choices[0])

# Write the output audio data to a file
wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("dog.wav", "wb") as f:
    f.write(wav_bytes)