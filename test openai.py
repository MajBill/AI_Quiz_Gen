# from openai import OpenAI
# from pydantic import BaseModel
# import server

# client = OpenAI()
# client = OpenAI(
#     base_url="http://127.0.0.1:1234",  #"http://localhost:1234/v1",
#     api_key = "sk-lm-5LwqapLc:8Oqtunxk7au4WeFZDQYP",  #"placeholder"
#     )
# print("OpenAI client created successfully!")
# print(f"Using API key: {client.api_key[:8]}...")

# import os
# import requests
# import json

# response = requests.post(
#   "http://localhost:1234/api/v1/chat",
#   headers={
#     "Authorization": f"Bearer {"sk-lm-5LwqapLc:8Oqtunxk7au4WeFZDQYP"}",
#     "Content-Type": "application/json"
#   },
#   json={
#     "model": "llama-3.2-3b-instruct",
#     "input": "Write a short Python function to add two integers."
#   }
# )
# content = response.json()['output'][0]['content']
# # print(json.dumps(response.json(), indent=2))
# print(content)
# 

# import server

# req = server.ChatRequest(prompt = "Generate 5 math quiz questions")

# resp = server.chat(req)

# print()


user_name = "Bill"
destination = "Italy"

prompt = f"""
You are a travel planner.

The traveler is:
Name: {user_name}
Destination: {destination}

Respond ONLY with valid JSON.

{
  "name": "",
  "destination": "",
  "recommended_cities": [],
  "estimated_budget": "",
  "reasoning": ""
}

"""

import json

body = {
    "model": "qwen2.5-7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "You always follow the requested output format exactly."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.2
}

json_body = json.dumps(body)

# import requests

# url = "http://localhost:1234/v1/chat/completions"

# prompt = f"""
# The customer is 77 years old.

# Return the answer in exactly this format:

# Name:
# Age:
# Recommendation:
# Reason:
# """

# body = {
#     "model": "qwen2.5-7b-instruct",
#     "messages": [
#         {
#             "role": "system",
#             "content": "Follow the requested output format exactly."
#         },
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ],
#     "temperature": 0.2
# }

# response = requests.post(url, json=body)
# response.raise_for_status()

# answer = response.json()["choices"][0]["message"]["content"]

# print(answer)