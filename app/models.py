from pydantic import BaseModel

class MeetingRequest(BaseModel):
    user_input: str 