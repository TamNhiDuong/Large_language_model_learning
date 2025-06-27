from openai import OpenAI

client = OpenAI(
  # client initialization
  api_key="TOKEN",
)

MODEL = "gpt-4o" 

def prompt(message):
  response = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "user", "content": message},
    ]
  )

  return response.choices[0].message.content


print(prompt("Hi there!"))