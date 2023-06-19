import openai

openai.api_key = "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"

messages = [
    {"role": "system", "content": "프로그래밍 전문가가 되기 위한 도우미"}
]
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")

