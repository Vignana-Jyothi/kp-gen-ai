import requests

# Your Hugging Face API key
from config import HUGGINGFACE_API_KEY  


# The model you want to use
model = "distilbert-base-uncased-finetuned-sst-2-english"

# The text you want to classify
text = "I love so much using Hugging Face models!"

# Set up the headers and data for the request
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

data = {
    "inputs": text
}

# Make the request to the Hugging Face API
response = requests.post(
    f"https://api-inference.huggingface.co/models/{model}",
    headers=headers,
    json=data
)

# Parse the response
result = response.json()

print(result)
