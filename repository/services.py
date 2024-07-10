import os
import requests
from PIL import Image
from dotenv import load_dotenv
from transformers import AutoProcessor, AutoModelForCausalLM

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")

model_name = "notebooks/models/git-base-train"
processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def create_story(photos: dict):
    captions = []

    for image in photos:
        url = f"https://api.telegram.org/bot{TG_TOKEN}/getFile?file_id={image}"
        file_path = requests.get(url).json()["result"]["file_path"]
        photo_url = f"https://api.telegram.org/file/bot{TG_TOKEN}/{file_path}"

        image = Image.open(requests.get(photo_url, stream=True).raw)
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        captions.append(caption)

    return captions
