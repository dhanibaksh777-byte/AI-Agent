from sqlalchemy.orm import Session
from dotenv import load_dotenv
from models import Message,Conversation,Note
from tools.web_search import get_response,web_search_tool
from tools.datetime import current_time_date,datetime_tool
from tools.note_saver import save_note,save_note_tool
from tools.calculator import calculate,calculator_tool
from groq import Groq 
import os
import json


SYSTEM_PROMPT = """You are a helpful AI agent. You have access to the following tools:
- web_search: Search the web for real-time information
- calculate: Perform mathematical calculations
- current_time_date: Get the current date and time
- save_note: Save a note to the database

Use the appropriate tool when needed. If no tool is needed, answer directly."""

load_dotenv()

api_key = os.getenv("groq_api_key")
if not api_key :
    raise RuntimeError("groq api key does'nt found")
client = Groq(api_key=api_key)

def get_response(message : str, db : Session):
    Message = [{"role" : "system", "content" : SYSTEM_PROMPT},
               {"role" : "user", "content" : message}
               ]
    response = client.chat.completions.create(
        messages=Message
        model = "openai/gpt-oss-120",
        
    )
    
