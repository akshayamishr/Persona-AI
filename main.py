from HiteshChoudhary import personaPrompt 
from google import genai
from google.genai import types
from pydantic import BaseModel
import json


client = genai.Client(api_key="Your API Key here")

class responseStruture(BaseModel):
    step: str
    content : str


config = types.GenerateContentConfig(
    system_instruction = personaPrompt,
    response_mime_type="application/json",
    response_schema=responseStruture
)

messages = []



def getResponse():
    response = client.models.generate_content(
    model = "gemini-1.5-flash",
    contents = messages,
    config = config
)
    return response

def chat():

    while(True):
        userInput = input("You : ")
        messages.append(types.Content(
            role="user", 
            parts=[types.Part(text = userInput)]))

        response = getResponse()
        messages.append(response.candidates[0].content)
        parsed_response = json.loads(response.text)

        print("Hitesh Choudhary : " + parsed_response.get("content"))
            
        
chat()