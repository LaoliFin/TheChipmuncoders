from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os
import base64

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generatePrompt(lyrics):
    prompt = "Give me one ai image generating prompt based on this text, without using special characters: " + lyrics
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    print(response.text)
    return response.text

def generateImage(prompt):

    prompt = generatePrompt(prompt)
    contents = (prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image']
        )
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            image.save('./static/ai_image.png')
            image.show()

#prompt = generatePrompt("Sorry, your grandma died. RIP.")
#prompt = generatePrompt("I kissed a gull and I liked it.")
#generateImage(prompt)