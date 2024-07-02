import requests

# Your Hugging Face API key
from config import HUGGINGFACE_API_KEY  

def get_user_input(prompt):
    return input(prompt)

def make_api_request(endpoint, data):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    response = requests.post(
        f"https://api-inference.huggingface.co/models/{endpoint}",
        headers=headers,
        json=data
    )
    return response.json()

def sentiment_analysis():
    text = get_user_input("Enter text for sentiment analysis: ")
    data = {"inputs": text}
    result = make_api_request("distilbert-base-uncased-finetuned-sst-2-english", data)
    print(result)

def named_entity_recognition():
    text = get_user_input("Enter text for named entity recognition: ")
    data = {"inputs": text}
    result = make_api_request("dbmdz/bert-large-cased-finetuned-conll03-english", data)
    print(result)

def text_summarization():
    text = get_user_input("Enter text for summarization: ")
    data = {"inputs": text}
    result = make_api_request("facebook/bart-large-cnn", data)
    print(result)

def text_generation():
    text = get_user_input("Enter text for text generation: ")
    data = {"inputs": text, "parameters": {"max_length": 50, "num_return_sequences": 1}}
    result = make_api_request("openai-community/gpt2", data)
    print(result)

def question_answering():
    context = get_user_input("Enter context for question answering: ")
    question = get_user_input("Enter question: ")
    data = {"inputs": {"question": question, "context": context}}
    result = make_api_request("deepset/roberta-base-squad2", data)
    print(result)

def main():
    print("Choose a text analysis task:")
    print("1. Sentiment Analysis")
    print("2. Named Entity Recognition")
    print("3. Text Summarization")
    print("4. Text Generation")
    print("5. Question Answering")
    
    choice = get_user_input("Enter the number of your choice: ")

    if choice == '1':
        sentiment_analysis()
    elif choice == '2':
        named_entity_recognition()
    elif choice == '3':
        text_summarization()
    elif choice == '4':
        text_generation()
    elif choice == '5':
        question_answering()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
