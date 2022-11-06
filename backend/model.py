from pydantic import BaseModel
#orm
class Todo(BaseModel):
  title: str
  description: str
