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
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)