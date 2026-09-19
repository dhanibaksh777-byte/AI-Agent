from models import Note

def save_note(content : str,db):
    note = Note(content = content)
    db.add(note)
    db.commit()
    return note


save_note_tool = {
    "type" : "function",
    "function" : {
        "name" : "save_note",
        "description" : "for saving the note",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "content" : {
                    "type" : "string",
                    "description" : "for saving the user notes",
                }
            },
            "required" : ["content"]
        }
    }
}