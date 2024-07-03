import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import soundfile as sf

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)


# Path to your local WAV file
audio_file_path = "speech.wav"

# Load the audio file
audio_array, sample_rate = sf.read(audio_file_path)

# Process the audio array through the pipeline
result = pipe({"array": audio_array, "sampling_rate": sample_rate})
print(result["text"])

# Original Text
# VNRVJIET currently supports mentorship for B.Tech students through a system
# where each faculty member is assigned 20 students for the entirety 
# of their 4-year course. The current process involves students logging their 
# mentorship activities in a physical book, which mentors later transcribe into 
# the EduPrime online portal. This approach has several drawbacks

# Generated:
# Mindrevyet currently supports mentorship for B, tech students through a system
# where each faculty member is assigned students for the entirety of 
# their year course. The current process involves students logging their 
# mentorship activities in a physical book, which mentors later transcribe into
# the Eduprime online portal. This approach has several drawbacks 
    # of several drawbacks into the Eduprime online portal. 
    # This approach has several drawbacks as several drawbacks 
    # into the Eduprime online portal. This is a 
