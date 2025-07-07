
## Requirements
- Python > 3.10
- Docker (for API server) download it from ( https://drive.google.com/file/d/1MNt0fBJAjOu7pODx0HsStDLBemhAgBuR/view )

## Setup
1. Load & run the Docker container:
   ♦ Download the Docker Image from link
   ♦ Then open cmd on the location of that image 
   ♦ run this command to load that image   
        docker load -i lp-programming-challenge-1-1625610904.tar.gz
   ♦ Run this command to run docker file
        docker run --rm -p 3123:3123 -ti lp-programming-challenge-1
2. How to run code :
    ♦ First install all requriments 
    ♦ Make virtual environment if needed using command Line and this command
        py -m venv env 
    ♦ Activate environmet using 
        .\env\Scripts\activate 
    ♦ Install requirements using this command
        pip install -r requirements.txt
    ♦ Now Just run main file using
        python main.py


## How it works 

The program begins by fetching a list of animal IDs from a paginated endpoint on a locally running HTTP API server using Docker. It continues requesting pages until batch gets to 100 it then posts each 100 batch and will continue this until there aren't any pages left. For each animal ID retrieved, an additional request is made to fetch the detailed data for that specific animal. Once all animal details are collected, each entry is transformed the friends field and the born_at field as per instructions. After transformation, the data is grouped into batches of up to 100 animals and sent to a separate API endpoint using POST requests. The system includes automatic retry logic to handle server errors (such as HTTP 500–504) and delays, ensuring the entire dataset is reliably processed and loaded without crashing or skipping records.

## File Structure
main.py # Entrypoint script
api.py  # Handles HTTP requests & retries
models.py    # schemas for input/output
transform.py # Logic for transforming data
loader.py    # Batching and GET,POST logic
requirements.txt # for requriements and dependencies
README.md # For details 
