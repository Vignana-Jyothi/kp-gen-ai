# dataset_preparation.py
import os
from PIL import Image
from datasets import Dataset

# Load your dataset
image_files = [os.path.join("faces", file) for file in os.listdir("faces")]

# Preprocess images
def preprocess_images(image_files):
    images = []
    for image_file in image_files:
        image = Image.open(image_file).convert("RGB")
        image = image.resize((512, 512))
        images.append({"image": image})
    return images

dataset = Dataset.from_list(preprocess_images(image_files))

# Save the dataset for later use
dataset.save_to_disk("preprocessed_dataset")
