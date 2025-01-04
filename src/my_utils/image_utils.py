import base64
import os

from dotenv import load_dotenv
from IPython.display import Image, display  # type: ignore
from openai import OpenAI

load_dotenv()

client = OpenAI()
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))


def encode_image(image_path):
    ''' Function to encode the image '''
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def preview_image(image_path='image.png'):
    ''' Display the image '''
    return display(Image(filename=image_path))


def describe_image(image_path='image.png', prompt="What is in this image?"):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content
