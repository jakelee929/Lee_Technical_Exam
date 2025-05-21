## ASSUMPTIONS

1. User has a local MongoDB database on: mongodb://localhost:27017


## HOW TO SETUP

1. Install dependencies:
pip install -r requirements.txt

2. Create .env file:
MONGO_URI=mongodb://localhost:27017

3. Run the API:
uvicorn api.main:app --reload

4. In a seperate terminal, run the file watcher:
python service/watcher.py

