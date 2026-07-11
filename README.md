# Restaurants near you - JET

A Flask web app that searches UK restaurants by postcode using the Just Eat API, displaying results as Bootstrap cards.

## 1. The goal of the task

The main goal of the task is to access the API end point given, and then access the first 10 restaurants corresponding to the given postcode by user and display each restaurants attributes. For e.g. name, cuisine, address, rating

## 3. How to run the program
- Ensure you have Python 3.12+ installed (earlier versions may also work)
- Install dependencies: `pip install -r requirements.txt`
- Navigate to the project root directory
- Run the application: `python backend.py`  
  (if this does not work, try `python3 backend.py`)
- Open your browser and go to: `http://127.0.0.1:5000/`
- Enter a postcode to test the program

## 4. How to run the unit tests
- Navigate to the project root directory
- Run: `pytest tests/test_backend.py`
- If `pytest` is not recognised, run: `python -m pytest tests/test_backend.py`

## 6. How AI was used
- ai use was kept to a minimum in this project as it was quite simple. the main hurdle was to learn something new with flask, bootstrap and pytest. AI was mainly used as a learning resource for e.g. asking about syntax, debugging parts of code and explaining the why behind new things I was learning for flask/pytest.

- AI was used a little more to help with the creation of html boilerplate/ guiding the very basic design of the webpage using bootstrap (for e.g. the card design). However, every architectural decision was of my own.

- Finally AI was also used to help with formatting the readme.
