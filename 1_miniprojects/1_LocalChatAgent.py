from openai import OpenAI

from openai import OpenAI

# Ollama OpenAI-compatible client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy key required by SDK
)

def get_chat_response(user_message: str) -> str:
    response = client.chat.completions.create(
        model="llama3:8b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_message = input("Ask a question (type 'exit' to quit): ")
        if user_message.lower() == "exit":
            break

        reply = get_chat_response(user_message)
        print("Assistant:", reply)
