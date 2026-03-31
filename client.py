from openai import OpenAI
client=OpenAI(api_key="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")
completion=client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {"role":"system","content":"You are a virtual assistant named Jarvis skilled in general tasks like Alexa or google assistant"},
        {"role":"user","content":"What is coding"}
    ]
)
print(completion.choices[0].message.content)