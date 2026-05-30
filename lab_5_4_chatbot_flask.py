from flask import Flask, request, jsonify
from openai import OpenAI

"""
To run this, start the app
Use curl or something similar (Postman etc.)

curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d '{"message": "Yo Snoop, what is up?"}'


NOTE: feel free to change the personality to a teacher, convict, comedian, politician or whatever you like.
"""


app = Flask(__name__)
# Add this line to allow emojis and special characters in JSON responses
app.json.ensure_ascii = False

client = OpenAI()

conversation = [
    {
        "role": "system",
        "content": "You are Snoop Dog, you speak with his voice, you're fun, a bit sarcastic, but always helpful."
    }
]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    conversation.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=conversation
    )

    reply = response.output[0].content[0].text

    conversation.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
