import aisuite as ai
from dotenv import dotenv_values

config = dotenv_values(".env")
client = ai.Client()

models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]

messages = [
    {"role": "system", "content": "Respond in an Italian Accent."},
    {"role": "user", "content": "Tell me the probability of severe weather."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)
