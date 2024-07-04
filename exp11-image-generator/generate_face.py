# generate_face.py
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Load the fine-tuned Stable Diffusion model
fine_tuned_pipe = StableDiffusionPipeline.from_pretrained("./stable_diffusion_finetuned")
fine_tuned_pipe = fine_tuned_pipe.to("cuda")

# Function to generate a new face
def generate_face(prompt, num_inference_steps=50):
    with torch.autocast("cuda"):
        image = fine_tuned_pipe(prompt, num_inference_steps=num_inference_steps).images[0]
    return image

# Example usage
prompt = "A photorealistic face of a person"
generated_image = generate_face(prompt)
generated_image.show()

# Save the generated image
generated_image.save("fine_tuned_generated_face.png")
