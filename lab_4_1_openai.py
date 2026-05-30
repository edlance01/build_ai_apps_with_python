from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {
            "role": "user",
            "content": "Tell me a joke to kick off my AI programming class.",
        }
    ],
)

# The Responses API has a built-in helper to extract the final text easily
print(response.output_text)
