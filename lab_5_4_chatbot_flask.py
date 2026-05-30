from openai import OpenAI

client = OpenAI()

conversation = [
    {
        "role": "system",
        "content": "You are Snoop Dog, you speak with his voice, you're fun, a bit sarcastic, but always helpful."
    }
]

print("Snoop be ready.  Type 'exit' to stop.\n")

while(True):
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Snoop is out.")
        break

    conversation.append({"role" : "user", "content" : user_input})

    response = client.responses.create(model="gpt-5.4-mini", input=conversation)

    reply = response.output[0].content[0].text

    conversation.append({"role": "assistant", "content": "rpely"})
    print("Snoop:", reply) 
