from pydantic import BaseModel
from typing import Optional, List

# Models for the Animal 
class AnimalListing(BaseModel):
    id: str
    name: str
# Model for the Animal Details
class AnimalDetails(BaseModel):
    id: str
    name: str
    friends: Optional[str]
    born_at: Optional[str]
# Model for the Transformed Animal
class TransformedAnimal(BaseModel):
    id: str
    name: str
    friends: List[str]
    born_at: Optional[str]
