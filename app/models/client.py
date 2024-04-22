from pydantic import BaseModel
from fastapi import Form
from typing import Annotated

class Client(BaseModel):
    name: str
    last_name: str
    email: str

    @classmethod
    def as_form(
        cls,
        name: Annotated[str, Form(...)],
        last_name: Annotated[str, Form(...)],
        email: Annotated[str, Form(...)]
    ):
        
        return cls(
            name=name,
            last_name=last_name,
            email=email
        )
    
class ModifyClient(BaseModel):
    name: str | None = None
    last_name: str | None = None
    email: str | None = None

    @classmethod
    def as_form(
        cls,
        name: Annotated[str | None, Form(...)] = None,
        last_name: Annotated[str | None, Form(...)] = None,
        email: Annotated[str | None, Form(...)] = None
    ):
        
        return cls(
            name=name,
            last_name=last_name,
            email=email
        )