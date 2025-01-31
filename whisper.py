import os
from openai import AzureOpenAI
        

endpoint = "https://jcqu-m6jsngyu-eastus2.cognitiveservices.azure.com/"
api_key="6GcIQkWfuXx6B5ydmnuNATA9yC9vroBHp2YFCnuOM5pQOBJQCeDOJQQJ99BAACHYHv6XJ3w3AAAAACOGmm0r"
deployment = "whisper"


client = AzureOpenAI(
    api_key=api_key,  
    api_version="2024-02-01",
    azure_endpoint = endpoint
)

deployment_id = deployment
audio_test_file = "https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/sampledata/audiofiles/wikipediaOcelot.wav"
    
result = client.audio.transcriptions.create(
    file=open(audio_test_file, "rb"),            
    model=deployment_id
)
    
print(result)