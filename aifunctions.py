import logging

import dotenv
import openai

dotenv.load_dotenv()
client = openai.OpenAI()

def transcribe_audio(in_file):
    audio_data =  open(in_file, "rb")

    response = client.audio.transcriptions.create(
        file = audio_data,
        model = "whisper-1",
    )

    logging.debug(response)
    return response.text

def refine_keypoints(transcript):
    transcript = str(transcript)
    
    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "List the key points from the following dictated transcript:\n\n" + transcript
            }
        ]
    )

    logging.debug(response)
    return response.choices[0].message.content
