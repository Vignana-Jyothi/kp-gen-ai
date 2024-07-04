from transformers import BartTokenizer, BartForConditionalGeneration

# Load the tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')


def summarize_text(text, max_length=150, min_length=40, length_penalty=2.0, num_beams=4):
    # Encode the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=1024, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
    
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example usage
text = """
The story begins in the kingdom of Ayodhya, ruled by the wise and just King Dasharatha. Despite having three queens, Kaushalya, Kaikeyi, and Sumitra, Dasharatha is initially childless and yearns for an heir. His longing for a successor leads him to perform a grand sacrifice, which is a turning point in the epic. This sacrifice is not only a display of his devotion and desperation but also sets the stage for the divine intervention that follows. The gods, pleased with Dasharatha’s devotion, grant him four sons, each born to one of his queens, marking the beginning of a new era in Ayodhya.

To obtain children, Dasharatha performs a grand sacrifice, and soon after, his queens give birth to four sons: Kaushalya bears Rama, Kaikeyi gives birth to Bharata, and Sumitra has twins, Lakshmana and Shatrughna. The birth of these princes brings immense joy and relief to Dasharatha, who sees in them the future of his dynasty. The princes are not only a fulfillment of Dasharatha’s wishes but also symbolize the virtues and divine qualities that will define their lives. As they grow up, each prince displays unique traits and skills, foreshadowing their roles in the epic saga that unfolds.

The four princes grow up to be brave, virtuous, and deeply devoted to each other. Rama, the eldest, is especially beloved and revered by all for his noble character and prowess. His virtues are evident from a young age, earning him the admiration and respect of his family and the people of Ayodhya. Lakshmana, his inseparable companion, shares a special bond with Rama, marked by unwavering loyalty and support. Bharata, known for his righteousness, and Shatrughna, the youngest, are also esteemed for their virtues. Together, the brothers represent the ideal qualities of courage, devotion, and filial piety.

"""
summary = summarize_text(text)
print("Summary:", summary)
