import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = "https://azureopeaitrainer.openai.azure.com/", 
  api_key="b4c4fd358ba94e75af1fa5bfe0dd476d",  
  api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        { "role": "system", "content": "Eres mi asistente personal." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Describe la siguiente imágen:" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    #"url": "https://www.nippon.com/es/ncommon/contents/japan-glances/2456656/2456656.jpg"
                    "url": "https://aeroclubnimbus.aero/wp-content/uploads/2020/04/la.png"
                }
            }
        ] } 
    ],
    max_tokens=2000 
)

print(response)