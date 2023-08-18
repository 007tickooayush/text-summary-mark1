from pydantic import BaseModel

class Content(BaseModel):
    content:str
    min_length:int=None

