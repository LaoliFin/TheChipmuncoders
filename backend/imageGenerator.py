from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key='AIzaSyD6eObuVt5AkwUVqDjD4zkSp33zZ5qfG_c')

def generatePrompt(lyrics):
    prompt = "Give me one ai image generating prompt based on this text: " + lyrics
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    print(response.text)
    return response.text

def generateImage(prompt):

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
            image.save('gemini-native-image.png')
            image.show()

prompt = generatePrompt("[Verse 1] A long time ago when the Earth was green And there were more kinds of animals than youve ever seen Theyd run around free while the Earth was being born But the loveliest of them all was the Unicorn [Chorus] There were green alligators and long-necked geese Some humpty-backed camels and some chimpanzees Some cats and rats and elephants, but sure as youre born The loveliest of all was the Unicorn")

generateImage(prompt)