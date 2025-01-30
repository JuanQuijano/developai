import base64
import asyncio
from azure.core.credentials import AzureKeyCredential
from rtclient import (
    ResponseCreateMessage,
    RTLowLevelClient,
    ResponseCreateParams
)

endpoint = "https://azureopeaitrainer.openai.azure.com/"
api_key="b4c4fd358ba94e75af1fa5bfe0dd476d"
api_version="2024-02-01"
deployment = "gpt-4o-realtime-preview"

async def text_in_audio_out():
    async with RTLowLevelClient(
        url=endpoint,
        azure_deployment=deployment,
        key_credential=AzureKeyCredential(api_key)
    ) as client:
        await client.send(
            ResponseCreateMessage(
                response=ResponseCreateParams(
                    modalities={"audio", "text"}, 
                    instructions="Please assist the user."
                )
            )
        )
        done = False
        while not done:
            message = await client.recv()
            match message.type:
                case "response.done":
                    done = True
                case "error":
                    done = True
                    print(message.error)
                case "response.audio_transcript.delta":
                    print(f"Received text delta: {message.delta}")
                case "response.audio.delta":
                    buffer = base64.b64decode(message.delta)
                    print(f"Received {len(buffer)} bytes of audio data.")
                case _:
                    pass

async def main():
    await text_in_audio_out()

asyncio.run(main())