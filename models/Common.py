from pydantic import BaseModel
from typing import List, TypeVar, Generic

T = TypeVar('T', bound=BaseModel)

class CommonResponse(Generic[T], BaseModel):
    Status: str
    ErrorMessage: str
    Data: List[T]

