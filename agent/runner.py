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

def get_responses(message : str, db : Session,conv_id : str):
    message_list = [{"role" : "system", "content" : SYSTEM_PROMPT}]
    history = db.query(Message).filter(Message.conversation_id == conv_id).all()
    for msg in history:
        message_list.append({"role" : msg.role,"content" : msg.content})
    message_list.append({"role" : "user", "content" : message})

    while True:

        response = client.chat.completions.create(
            messages=message_list,
            model = "openai/gpt-oss-120b",
            tools=[web_search_tool, calculator_tool, datetime_tool, save_note_tool]

        )
        tool_Call = response.choices[0].message.tool_calls

        if not tool_Call:
            final_reply = response.choices[0].message.content
            db.add(Message(conversation_id=conv_id, role="user", content=message))
            db.add(Message(conversation_id=conv_id, role="assistant", content=final_reply))
            db.commit()
            return final_reply
    
        message_list.append(response.choices[0].message)
        tool_name = tool_Call[0].function.name
        arguments = json.loads(tool_Call[0].function.arguments)
        if tool_name == "web_search_tool":
            final_answer = get_response(arguments["query"])
            message_list.append({"role" : "tool", "content" : str(final_answer),"tool_call_id" : tool_Call[0].id})
        elif tool_name == "calculator_tool":
            final_answer = calculate(arguments["expressions"])
            message_list.append({"role" : "tool", "content" : str(final_answer),"tool_call_id" : tool_Call[0].id})
        elif tool_name == "datetime_tool":
            final_answer = current_time_date()
            message_list.append({"role" : "tool", "content" : str(final_answer),"tool_call_id" : tool_Call[0].id})
        elif tool_name == "save_note_tool":
            final_answer = save_note(arguments["content"],db)
            message_list.append({"role" : "tool", "content" : str(final_answer),"tool_call_id" : tool_Call[0].id})