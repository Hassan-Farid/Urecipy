from pytube import YouTube
import requests
import json
import os
import openai
from dotenv import load_dotenv

#Activating access to .env files
load_dotenv()

def get_video_from_url(video_url, filename):
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename="./audios/{}".format(filename))
    
def get_text_from_audio(video_url, filename):
    filename = "{}.mp4".format(filename)
    get_video_from_url(video_url, filename)
    whisper_url = "https://whisper.lablab.ai/asr"
    payload = {}
    files = [
        ('audio_file', (filename, open("./audios/{}".format(filename), 'rb'), 'audio/mpeg'))
    ]
    response = requests.request("POST", whisper_url, data=payload, files=files)
    return dict(json.loads(response.text))['text']

def get_audio_completion(gpt_prompt):
    openai.api_key = os.environ.get('OPENAI_SECRET_KEY')
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=gpt_prompt,
                                        temperature=0.0,
                                        max_tokens=2048,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0,
                                       )
    return response

def get_recipe_completion(audio_text):
    ingredient_prompt = "What unique ingredients are used in the recipe (Give answer in a single line with space between each ingredient name): {}".format(audio_text)
    procedure_prompt = "What is the cooking procedure explained in the recipe (Give answer in a single paragraph): {}".format(audio_text)
    return get_audio_completion(ingredient_prompt), get_audio_completion(procedure_prompt)

def get_ingredients(recipe_ingredients):
    return dict(recipe_ingredients['choices'][0])['text'].replace('-','').replace(':','')

def get_procedure(recipe_procedure):
    return dict(recipe_procedure['choices'][0])['text'].replace('\n', ' ')