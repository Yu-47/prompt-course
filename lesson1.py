from utils import *

client = get_client()

def fake_mutip_round_conversation(model="deepseek-flash"):
    messages = [
        {"role": "user", "content": "我叫小明"},
        {"role": "assistant", "content": "你好小红，很高兴认识你！"},
        {"role": "user", "content": "我叫什么名字？"},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    print(response.choices[0].message.reasoning_content)
    print("-------------以上是reasoning-------------")

    return response.choices[0].message.content

print(get_completion("用一句话解释什么是大语言模型"))
print(fake_mutip_round_conversation())

# -------------以下是多轮对话-------------

messages_list = []
def mutip_round_conversation(input_messages, model="deepseek-flash"):
    response = client.chat.completions.create(
        model=model,
        messages=input_messages,
        temperature=0,
    )
    print(response.choices[0].message.reasoning_content)
    print("-------------以上是reasoning-------------")
    print("这是token用量")
    print(response.usage.prompt_tokens)

    return response.choices[0].message.content

while True:
    user_input = input("你：")
    if user_input == "exit":
        break

    messages_list.append({"role": "user", "content": user_input})
    response = mutip_round_conversation(messages_list)

    print(response)

    messages_list.append({"role": "assistant", "content": response})