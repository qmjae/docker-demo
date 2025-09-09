from sqlmodel import SQLModel, Field

class ChatMessagePayload(SQLModel):
    #pydantic model
    # validation model for incoming chat message payload
    message: str

class ChatMessage(SQLModel, table=True):
    #db table
    #saving, updating, deleting chat messages
    id: int | None = Field(default=None, primary_key=True)
    message: str
