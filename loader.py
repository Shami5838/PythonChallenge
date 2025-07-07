from api import get_animal_page, get_animal_details, post_animals_home
from models import AnimalDetails
from transform import transform_animal
from more_itertools import chunked
import datetime


def start_process():
    page = 1 # starting of page
    batch = [] # list for batches
    total_posted = 0 # keep track of total posted animals
    current_fetched =0 # keep track of current fetched animals
    
    while True: # loop to fetch and process animals page by page
        print(f"Fetching page {page}")
        page_data = get_animal_page(page)
        if not page_data or not page_data["items"]:
            break
        print(f"Processing page {page} with {len(page_data['items'])} animals")
        current_fetched += len(page_data["items"])
        print(f"Total animals fetched so far : {current_fetched} appending to batch\n\n")
        
        for animal in page_data["items"]:
            animal_id = animal["id"]
            raw = get_animal_details(animal_id)
            raw["id"] = str(raw["id"])
            if "born_at" in raw and raw["born_at"] is not None:
                try:
                    ts = int(raw["born_at"])
                    if ts > 1e12:
                        ts = ts // 1000
                    if ts > 0:
                        raw["born_at"] = datetime.datetime.utcfromtimestamp(ts).replace(tzinfo=datetime.timezone.utc).isoformat()
                    else:
                        raw["born_at"] = None
                except Exception as e:
                    print(f"Invalid born_at value for animal {raw['id']}: {raw['born_at']} ({e})")
                    raw["born_at"] = None
            detail = AnimalDetails(**raw)

            batch.append(transform_animal(detail).dict())
            # POST THE BATCH OF 100 ANIMALS
            if len(batch) == 100:
                current_fetched = 0
                print(f"Posting final batch of {len(batch)} animals (total posted: {total_posted + len(batch)})")
                resp,status = post_animals_home(batch)
                print(f'API Response: {resp.get("message")} | API STATUS: {status}\n\n')
                total_posted += 100
                batch = []

        page += 1

    # Post any remaining animals
    if batch:
        current_fetched = 0
        print(f"Posting final batch of {len(batch)} animals (total posted: {total_posted + len(batch)})")
        resp,status = post_animals_home(batch)
        print(f'API Response: {resp.get("message")} | API STATUS: {status}\n\n')
        

