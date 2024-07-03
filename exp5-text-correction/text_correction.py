# Install Required Libraries
# pip install transformers
# pip install torch
# pip install sentence-transformers

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from sentence_transformers import SentenceTransformer, util

# Load pre-trained model and tokenizer
model_name = "facebook/bart-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Source of truth sentences
source_of_truth = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is transforming the world.",
    "Data science involves statistics, programming, and domain knowledge.",
    # Add more sentences as needed
]

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

# Test the function
input_sentence = "The quikc brwon fox jump ovr the lazi dog."
corrected_sentence = correct_sentence(input_sentence, source_of_truth, model, tokenizer)
print(f"Corrected Sentence: {corrected_sentence}")
