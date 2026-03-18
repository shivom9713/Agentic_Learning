import uuid
from pydantic import BaseModel, Field
import yaml, os

def create_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

# print(isinstance(create_thread_id(),uuid.UUID))


class ChatName(BaseModel):
    chat_name: str = Field(
        description="A concise, human-readable title summarizing the chat.",
        min_length=3,
        max_length=60,
    )

FILE_PATH = "thread_map.yaml"

def load_or_create_yaml(path=FILE_PATH):
    # If file doesn't exist, create it
    if not os.path.exists(path):
        base_structure = {"chats": {}}
        with open(path, "w") as f:
            yaml.dump(base_structure, f)
        return base_structure
    
    # Load existing file
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    # Ensure chats key exists
    if data is None:
        data = {"chats": {}}
    elif "chats" not in data:
        data["chats"] = {}

    return data


def update_chat_thread(id, chat_name="NA", path=FILE_PATH):#other_field=None,
    data = load_or_create_yaml(path)
    updated = False

    if id in data["chats"]:
        updated = True
        data["chats"][id]["chatname"] = chat_name
        data["chats"][id]["is_updated"] = updated
            # Save back to file
        with open(path, "w") as f:
            yaml.dump(data, f)
    

    return updated

def get_chat_thread(id, path=FILE_PATH):#other_field=None,
    data = load_or_create_yaml(path)

    if id in data["chats"]:
        return data["chats"][id]

            




def append_chat_thread(id, chat_name = "NA", path=FILE_PATH):
    data = load_or_create_yaml(path)
    if id not in data["chats"]:
        data["chats"][id] = {"chatname": chat_name, "is_updated": False} #, "other_field" : "NAN"
            # Save back to file
        with open(path, "w") as f:
            yaml.dump(data, f)
    else:
        print(f"key: {id} exists already")


