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
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Describe this picture:" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    "url": ""
                }
            }
        ] } 
    ],
    max_tokens=2000 
)

print(response)