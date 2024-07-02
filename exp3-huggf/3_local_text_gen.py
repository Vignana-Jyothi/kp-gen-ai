from transformers import pipeline

def get_user_input(prompt):
    return input(prompt)

def sentiment_analysis():
    classifier = pipeline("sentiment-analysis")
    text = get_user_input("Enter text for sentiment analysis: ")
    result = classifier(text)
    print(result)

def named_entity_recognition():
    ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)
    text = get_user_input("Enter text for named entity recognition: ")
    result = ner(text)
    print(result)

def text_summarization():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text = get_user_input("Enter text for summarization: ")
    result = summarizer(text)
    print(result)

def text_generation():
    generator = pipeline("text-generation", model="openai-community/gpt2")
    text = get_user_input("Enter text for text generation: ")
    result = generator(text, max_length=50, num_return_sequences=1)
    print(result)

def question_answering():
    qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    context = get_user_input("Enter context for question answering: ")
    question = get_user_input("Enter question: ")
    result = qa(question=question, context=context)
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
