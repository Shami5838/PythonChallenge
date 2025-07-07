from models import AnimalDetails, TransformedAnimal
from datetime import datetime, timezone

# Function transform_animal is used to transform an AnimalDetails object into a TransformedAnimal object.
def transform_animal(animal: AnimalDetails) -> TransformedAnimal:
    friends_list = (
        [f.strip() for f in animal.friends.split(",")] if animal.friends else []
    )
    born_at_iso = (
        datetime.fromisoformat(animal.born_at)
        .astimezone(timezone.utc)
        .isoformat()
        if animal.born_at else None
    )
    return TransformedAnimal(
        id=animal.id,
        name=animal.name,
        friends=friends_list,
        born_at=born_at_iso
    )
