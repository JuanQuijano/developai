from openai import AzureOpenAI
import os
import requests
from PIL import Image
import json

client = AzureOpenAI(
  azure_endpoint = "https://azureopeaitrainer.openai.azure.com/", 
  api_key="b4c4fd358ba94e75af1fa5bfe0dd476d",  
  api_version="2024-02-01"
)


result = client.images.generate(
    model="dalle3", # the name of your DALL-E 3 deployment
    prompt="Un primer plano de una conejo huyendo de un lobo que lo persigue por un bosque oscuro, mientras un aguila lo observa fíjamente",
    n=1
)

json_response = json.loads(result.model_dump_json())

image_dir = os.path.join(os.curdir, 'images')

if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

image_path = os.path.join(image_dir, 'generated_image.png')

image_url = json_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

image = Image.open(image_path)
image.show()