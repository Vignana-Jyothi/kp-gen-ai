import torch
from datasets import load_from_disk, Dataset
from diffusers import StableDiffusionPipeline
from transformers import TrainingArguments, Trainer
from PIL import Image

# Load the pre-trained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")

# Load the preprocessed dataset
dataset = load_from_disk("preprocessed_dataset")

# Define a function to preprocess images for training
def preprocess_images(examples):
    images = [Image.open(image).convert("RGB") for image in examples["image"]]
    inputs = pipe.tokenizer(images, return_tensors="pt")
    return inputs

# Apply the preprocessing function to the dataset
dataset = dataset.map(preprocess_images, batched=True)

# Define the training arguments
training_args = TrainingArguments(
    output_dir="./stable_diffusion_finetuned",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    logging_dir='./logs',
)

# Define the Trainer
trainer = Trainer(
    model=pipe.unet,  # or the appropriate model component
    args=training_args,
    train_dataset=dataset["train"],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./stable_diffusion_finetuned")
