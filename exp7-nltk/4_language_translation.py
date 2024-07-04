from transformers import MarianMTModel, MarianTokenizer

# Function to perform translation
def translate(texts, src_lang, tgt_lang):
    # Load the pre-trained MarianMT model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    # Tokenize the text
    translated = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated_tokens = model.generate(**inputs)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        translated.append(translated_text)
    
    return translated

# Sample text data
texts = [
    "Hello, how are you?",
    "This is a test sentence.",
    "I love programming."
]

# Translate from English to French
translated_texts_fr = translate(texts, src_lang="en", tgt_lang="fr")

# Translate from English to Hindi
translated_texts_hi = translate(texts, src_lang="en", tgt_lang="hi")

# Print the translations for French
print("Translations to French:")
for i, text in enumerate(translated_texts_fr):
    print(f"Original: {texts[i]}")
    print(f"Translated: {text}\n")

# Print the translations for Hindi
print("Translations to Hindi:")
for i, text in enumerate(translated_texts_hi):
    print(f"Original: {texts[i]}")
    print(f"Translated: {text}\n")
