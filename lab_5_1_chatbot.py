from openai import OpenAI

client = OpenAI()

print("Snoop be ready.  Type 'exit' to stop.\n")

while(True):
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Snoop is out.")
        break

    response = client.responses.create(model="gpt-5.4-mini", input=user_input)

    reply = response.output[0].content[0].text
    print("Snoop:", reply)
