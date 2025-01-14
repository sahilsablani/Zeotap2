CDP Chatbot
A Flask-based API that enables users to query documentation for various Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. The chatbot scrapes, indexes, and searches documentation to provide relevant answers to user queries.

Table of Contents
Features
File Structure
Setup Instructions
API Usage
Testing
Technologies Used
Features
Scrapes documentation from supported CDPs (Segment, mParticle, Lytics, Zeotap).
Efficient search functionality to retrieve answers from indexed documentation.
API for querying documentation with user questions.
Modular and extensible design for adding more CDPs.
File Structure
bash
Copy code
cdp_chatbot/
├── app.py                           # Main Flask app entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── configs/
│   ├── scraper_config.json          # Configuration for scraper URLs
│   ├── logging_config.json          # Logging settings
├── scraper/
│   ├── __init__.py                  # Marks this as a Python package
│   ├── segment_scraper.py           # Logic to scrape Segment docs
│   ├── mparticle_scraper.py         # Logic to scrape mParticle docs
│   ├── lytics_scraper.py            # Logic to scrape Lytics docs
│   ├── zeotap_scraper.py            # Logic to scrape Zeotap docs
├── indexer/
│   ├── __init__.py                  # Marks this as a Python package
│   ├── content_indexer.py           # Indexes and searches scraped content
└── tests/
    ├── test_app.py                  # Unit tests for Flask endpoints
    ├── test_scraper.py              # Unit tests for scraper logic
Setup Instructions
Prerequisites
Python 3.9 or above installed.
Postman for API testing.
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/cdp-chatbot.git
cd cdp-chatbot
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Run the Flask app:

bash
Copy code
python app.py  
Access the app at http://127.0.0.1:5000.

API Usage
1. Query Endpoint
URL: /query
Method: POST

Request Body (JSON):

json
Copy code
{
  "cdp": "segment",
  "question": "How do I set up a source?"
}
Response (JSON):

json
Copy code
{
  "answer": "Steps to set up a source in Segment..."
}
Error Example:
If an invalid CDP name is provided:

json
Copy code
{
  "error": "Invalid CDP name 'unknown'. Supported CDPs: segment, mparticle, lytics, zeotap"
}
2. Default Route
URL: /
Method: GET
Returns a welcome message:

css
Copy code
Welcome to the CDP Chatbot! Ask how-to questions about Segment, mParticle, Lytics, or Zeotap.
Testing
Using Postman
Start the Flask server with python app.py.
Open Postman and create a POST request to http://127.0.0.1:5000/query.
Add the following JSON to the Body tab:
json
Copy code
{
    "cdp": "segment",
    "question": "What are integrations in Segment?"
}
Click Send and view the response.
Running Unit Tests
Run tests using pytest:
bash
Copy code
pytest tests/
Technologies Used
Flask: Python web framework for building the API.
Postman: Testing API endpoints.
pytest: Unit testing framework for Python.
