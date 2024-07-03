from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from sentence_transformers import SentenceTransformer, util

# Function to read sentences from a file
def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

# Load pre-trained model and tokenizer
model_name = "facebook/bart-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Load sentences from files
source_of_truth = read_sentences_from_file('source_of_truth.txt')
input_sentences = read_sentences_from_file('input.txt')

# Load a sentence transformer model for similarity comparison
sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to correct sentences
def correct_sentence(input_sentence, source_of_truth, model, tokenizer):
    # Encode the input sentence
    inputs = tokenizer(input_sentence, return_tensors='pt')
    
    # Generate the corrected sentence
    with torch.no_grad():
        outputs = model.generate(**inputs)
    corrected_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Compute embeddings for the corrected sentence and source of truth sentences
    embeddings_corrected = sentence_model.encode(corrected_sentence, convert_to_tensor=True)
    embeddings_source = sentence_model.encode(source_of_truth, convert_to_tensor=True)
    
    # Find the closest match from the source of truth sentences
    cos_scores = util.pytorch_cos_sim(embeddings_corrected, embeddings_source)[0]
    best_match_idx = torch.argmax(cos_scores).item()
    
    return source_of_truth[best_match_idx]

# Process each input sentence and print the corrected sentence
for input_sentence in input_sentences:
    corrected_sentence = correct_sentence(input_sentence, source_of_truth, model, tokenizer)
    print(f"Input Sentence: {input_sentence}")
    print(f"Corrected Sentence: {corrected_sentence}\n")
