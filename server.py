#strictly for server initialization 

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
app = FastAPI()

#connect to lmstudio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key = "placeholder"
    )

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

@app.post("/chat")
def chat(request: ChatRequest):
    response = client.chat.completions.create(
        model="gemma-3-27b-it-ultra-uncensored-heretic-i1",
        messages=[
            {"role": "user", "content": "you are a quiz generator"},
            {"role": "user", "content": request.prompt}
        ],
        max_tokens=request.max_tokens,
        temperature=0.7
    )
    return {"response": response.choices[0].message.content}
