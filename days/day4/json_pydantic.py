import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No API Available")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
#Define Structure
from pydantic import  BaseModel
class Info(BaseModel):
     Name:str
     Occupation: str
     EmailID: str
     Contact_Number: str

schema = Info.model_json_schema()
response_format={
     "type": "json_object"
}

system_prompt=f"""Extract the personal information from the info strictly based on this schema and give a json output.
{schema}
"""
message_system={
     "role":"system",
     "content":system_prompt
}

text="Hello! I am Divya Parmar, I am a Student and want to learn about AI. My emailID is abc@gmail.com. My contact number is XXXXXXXXXX. "
prompt=f""" This is ID card. Please extract the personal information from this.
{text}
 """
message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
print(response)

print("#############################")
answer=response.choices[0].message.content
print(answer)