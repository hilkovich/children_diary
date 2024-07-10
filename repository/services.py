import os
import json
import requests
from PIL import Image
from dotenv import load_dotenv
from transformers import AutoProcessor, AutoModelForCausalLM

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
ID_CATALOG_YANDEX = os.environ["ID_CATALOG_YANDEX"]
API_KEY_YANDEX = os.environ["API_KEY_YANDEX"]

model_name = "notebooks/models/git-base-train"
processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def tg_photo_url(photo_file_id: str):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/getFile?file_id={photo_file_id}"
    file_path = requests.get(url).json()["result"]["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TG_TOKEN}/{file_path}"
    return photo_url


def gen_captions(photos: dict):
    captions = []

    for image in photos:
        image = Image.open(requests.get(tg_photo_url(image), stream=True).raw)
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        captions.append(caption)

    return captions


def gen_story(message: str):
    prompt = {
        "modelUri": f"gpt://{ID_CATALOG_YANDEX}/yandexgpt/latest",
        "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "2000"},
        "messages": [
            {
                "role": "system",
                "text": "Ты русский писатель детских рассказов. Всегда возвращаешь текст только на русском.",
            },
            {
                "role": "user",
                "text": message,
            },
        ],
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY_YANDEX}",
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = json.loads(response.text)

    return result["result"]["alternatives"][0]["message"]["text"]


def gen_message(captions, descript):
    setup_input = "В тексте не использовать слова фотография, изображение, затем"

    message = f"""
            Напиши развернутое описание от первого лица происходящего на {len(captions)} фотографиях объединив в сюжет.
            Описания фотографий: {captions}.
            Дополнительное описание к фотографий: {descript}.
            Дополнительные требования: {setup_input}.
            """

    return message
