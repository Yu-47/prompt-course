import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

def _get_api_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['DEEPSEEK_API_KEY']

def get_client():
    client = OpenAI(
        api_key=_get_api_key(),
        base_url="https://api.deepseek.com",
    )

    return client

client = get_client()

def get_completion(prompt, output_fmt=False, model="deepseek-flash"):
    messages = [{"role": "user", "content": prompt}]
    if output_fmt == False:
        fmt =  { "type": "text" } 
    else:
        fmt =  { "type": "json_object" } 

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format=fmt,
        temperature=0,
    )
    # print(response)
    print(response.choices[0].message.reasoning_content)
    print("-------------以上是reasoning-------------")

    return response.choices[0].message.content
