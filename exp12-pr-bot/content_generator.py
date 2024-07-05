import os
import json
from dotenv import load_dotenv
import openai
from uuid import uuid4

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

def parse_whatsapp_messages(file_path):
    with open(file_path, 'r') as file:
        messages = json.load(file)
    return messages

def generate_content(parsed_data):
    content_list = []
    for data in parsed_data:
        prompt = f"Create a LinkedIn post based on the following information: {data['text']}"
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content_list.append({
            'id': str(uuid4()),
            'content': response.choices[0].message['content'],
            'timestamp': data['timestamp']
        })
    return content_list

def save_generated_content(content_list, output_path):
    with open(output_path, 'w') as file:
        json.dump(content_list, file, indent=4)

def main():
    parsed_data = parse_whatsapp_messages('input_data/whatsapp_messages.json')
    content_list = generate_content(parsed_data)
    save_generated_content(content_list, 'pr_content_generated.json')

if __name__ == "__main__":
    main()
