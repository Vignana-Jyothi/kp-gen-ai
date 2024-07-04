from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Function to perform translation
def translate(texts, src_lang, tgt_lang):
    # Load the pre-trained mBART model and tokenizer
    model_name = 'facebook/mbart-large-50-many-to-many-mmt'
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    
    # Set the source and target language tokens
    tokenizer.src_lang = src_lang
    translated = []
    
    for text in texts:
        # Tokenize the text
        inputs = tokenizer(text, return_tensors="pt")
        
        # Generate translation
        translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang])
        
        # Decode the tokens to text
        translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        translated.append(translated_text)
    
    return translated

# Sample text data
texts = [
    "Hello, how are you?",
    "This is a test sentence.",
    "I love programming."
]

# Translate from English to French
translated_texts_fr = translate(texts, src_lang="en_XX", tgt_lang="fr_XX")

# Translate from English to Hindi
translated_texts_hi = translate(texts, src_lang="en_XX", tgt_lang="hi_IN")

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
