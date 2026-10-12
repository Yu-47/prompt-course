import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

def get_api_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['DEEPSEEK_API_KEY']

def get_client():
    client = OpenAI(
        api_key=get_api_key(),
        base_url="https://api.deepseek.com",
    )

    return client


