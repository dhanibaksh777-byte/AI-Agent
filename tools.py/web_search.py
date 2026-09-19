from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("tavily_api_key")
if not api_key:
    raise RuntimeError("tavliy api key does'nt exists check your .env file")

def get_response(query : str):
    tavliy_Client = TavilyClient(api_key=api_key)
    response = tavliy_Client.search(query)
    return str(response["results"][0]["content"])


web_search_tool = {
    "type" : "function",
    "function" : {
        "name" : "web_search_tool",
        "description" : "search the web for the real time information",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "query" : {
                    "type" : "string",
                    "description" : "the search query",
                }
            },
            "required" : ["query"]
        }
    }
}