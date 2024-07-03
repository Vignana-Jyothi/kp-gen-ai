import requests

# Your Hugging Face API key
from config import HUGGINGFACE_API_KEY  
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
import requests

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

def query(audio):
    response = requests.post(API_URL, headers=headers, data=audio)
    return response.json()

# Path to your audio file
audio_input = "speech.wav"

try:
    # Load your audio file
    with open(audio_input, "rb") as f:
        audio_data = f.read()
    
    # Send the audio data to the Hugging Face API
    result = query(audio_data)
    print(result)

except FileNotFoundError:
    print(f"Error: The file {audio_input} was not found. Please ensure the file exists and the path is correct.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# ## Original Text
# VNRVJIET currently supports mentorship for B.Tech students through a system
# where each faculty member is assigned 20 students for the entirety 
# of their 4-year course. The current process involves students logging their 
# mentorship activities in a physical book, which mentors later transcribe into 
# the EduPrime online portal. This approach has several drawbacks

# ## Generated
# Mindrevyet currently supports mentorship for B, tech students through a system
# where each faculty member is assigned students for the entirety 
# of their year course. The current process involves students logging their
# mentorship activities in a physical book, which mentors later transcribe into
# the Eduprime online portal. This approach has several drawbacks
    # of several drawbacks into the Eduprime online portal. This is a roboviat.