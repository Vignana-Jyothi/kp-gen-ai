from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
from config import OPENAI_API_KEY  # Ensure this file contains your OpenAI API key

# Set your API key

def summarize_text(text, model):
    response = client.chat.completions.create(model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
    ],
    max_tokens=150  # Adjust token limit as needed)
    summary = response.choices[0].message.content.strip()
    return summary

# Example usage:
text_to_summarize = "Tommy was a boy with an insatiable love for sweets. From dawn till dusk, his pockets bulged with candies, chocolates, and cookies. His chubby cheeks and round belly spoke of his indulgence. Despite knowing he was already overweight, Tommy couldn’t resist the allure of sugar. One day, while savoring a giant lollipop, he caught his reflection and sighed. Determined to change, Tommy decided to balance his love for sweets with healthier choices and exercise. With every step, he found joy in his progress, proving that change, though challenging, was possible. His journey had just begun, sweet and steady."
model = "gpt-3.5-turbo"  # or "gpt-4-turbo", "gpt-3.5-turbo"
summary = summarize_text(text_to_summarize, model)
print("Summary:", summary)

