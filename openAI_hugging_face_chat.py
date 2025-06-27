import requests  # Import the library to make HTTP requests

# === Configuration ===
API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

# Replace with your Hugging Face API token (create one at https://huggingface.co/settings/tokens)
API_TOKEN = "TOKEN"

# Set the HTTP headers required by the Hugging Face API
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# === Start chatbot ===
print("🤖 Simple Phi-3 Chatbot — type 'exit' to quit.")

# Run a loop to keep chatting with the user
while True:
    # Ask the user for input
    user_input = input("You: ")

    # Exit the loop if the user types "exit"
    if user_input.lower() == "exit":
        break

    # Format the input in a way the model understands
    prompt = f"[INST] {user_input} [/INST]"

    # Create the data payload to send to the API
    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100  # Limit how long the response can be
        }
    }

    # Send a POST request to the Hugging Face inference API
    response = requests.post(API_URL, headers=headers, json=data)

    # Convert the response to JSON format (list of dicts)
    result = response.json()

    # Try to extract the generated text and print it
    try:
        # The model's reply is in the first item of the list, in the 'generated_text' field
        bot_reply = result[0]["generated_text"]
        print("Bot:", bot_reply)
    except Exception as e:
        # If something goes wrong, print the raw error
        print("Error:", result)
