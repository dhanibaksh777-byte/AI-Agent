from datetime import datetime,timezone
def current_time_date():
    current_date_time = datetime.now(timezone.utc)
    return current_date_time

datetime_tool = {
    "type": "function",
    "function" : {
        "name" : "current_time_date",
        "description" : "get current time and date",
        "parameters" : {
            "type" : "object",
            "properties" : {},
            "required" : []
        }
        
    }
}