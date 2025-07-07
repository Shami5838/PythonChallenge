import httpx
from tenacity import retry, stop_after_attempt, wait_random
from typing import List

BASE_URL = "http://localhost:3123" # BASE URL for the API


# API functions with retry logic to get the animals from page
@retry(stop=stop_after_attempt(5), wait=wait_random(1, 5))
def get_animal_page(page: int):
    resp = httpx.get(f"{BASE_URL}/animals/v1/animals?page={page}", timeout=30)
    resp.raise_for_status()
    return resp.json()

# API functions with retry logic to get the animal details by ID
@retry(stop=stop_after_attempt(5), wait=wait_random(1, 5))
def get_animal_details(animal_id: str):
    resp = httpx.get(f"{BASE_URL}/animals/v1/animals/{animal_id}", timeout=30)
    resp.raise_for_status()
    return resp.json()

# API functions with retry logic to POST BATCH of 100 animals to the home endpoint
@retry(stop=stop_after_attempt(5), wait=wait_random(1, 5))
def post_animals_home(batch: List[dict]):
    resp = httpx.post(f"{BASE_URL}/animals/v1/home", json=batch, timeout=60)
    
    resp.raise_for_status()
    data = resp.json()
    return data , resp.status_code
