
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=150, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = "Paris is the capital of France. "
    generated_text = generate(prompt)
    print("Generated Text:", generated_text)
