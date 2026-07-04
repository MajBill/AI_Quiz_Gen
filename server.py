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
        model="qwen2.5-3b-instruct",
        messages=[
            {"role": "system", "content": (
            "You are a quiz generator. "
            "Return ONLY valid JSON. No markdown, no explanations. "
            "STRICT RULES: "
            "1. Use ONLY double quotes (\") for all strings "
            "2. Do NOT use smart quotes or apostrophes "
            "3. Output must be valid JSON that can be parsed by json.loads() "
            "4. No trailing commas "
            "5. Answer must exactly match one option "
            "FORMAT: "
            "["
            "{"
            "\"question\": string, "
            "\"options\": array of 4 strings, "
            "\"answer\": string"
            "}"
            "]"
            # "[{"
            # "\"question\": string, "
            # "\"options\": [string, string, string, string], "
            # "\"answer\": string"
            # "}]"
            )},
            {"role": "user", "content": request.prompt}
        ],
        max_tokens=request.max_tokens,
        temperature=0.0
    )
    return {"response": response.choices[0].message.content}
