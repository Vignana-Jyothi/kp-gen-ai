from transformers import pipeline

# Load your text data
with open('ramayana_mini.txt', 'r') as file:
    context = file.read()

# Initialize the question-answering pipeline with a pre-trained model
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")

# Example questions
questions = [
    "What is the main topic of the text?",
    "Who are the main characters?",
    "What happened in the end?",
    "Tell me about Hanuman",
]

# Get answers for each question
for question in questions:
    result = qa_pipeline(question=question, context=context)
    print(f"Question: {question}")
    print(f"Answer: {result['answer']}\n")

