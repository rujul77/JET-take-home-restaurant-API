
from backend import app
from unittest.mock import patch
import requests

'''
going to include some very basic testing. four main things to look out for 

1 - make sure our route Get/ works
2 - if postcode is empty, will it handle it correctly?
3 - if correct postcode entered, will it show the restaurants?
4 - what if the api/network fails?
'''

#testing if our main homepage is loading/working fine.
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

#checking it will return whats excepted if postcode is empty
def test_empty_postcode():
    client = app.test_client() #mock browser
    response = client.post("/", data={"postcode": ""})
    assert b"Please enter a postcode!" in response.data

#does entering the correct postcode returna list of restaurants?
@patch("backend.restaurant_list") #patch replaces the function with a fake version
def test_correct_postcode(fake_res_list):

    #sending requests without a live server
    client = app.test_client()
    fake_list = [
    {
        "name": "KFC",
        "cuisines": "Chicken",
        "rating": "4.5",
        "address": "1 High Street, SW1A1AA",
        "logo": "kfc_logo.jpg"
    },
    {
        "name": "McDonalds",
        "cuisines": "Burgers",
        "rating": "4.2",
        "address": "2 Main Road, SW1A1AA",
        "logo": "mcd_logo.jpg"
    }
    ]

    fake_res_list.return_value = fake_list #making sure that the fake list is being used instead of the real api when running this test 

    #simulating the function in the fake server, ie we go the api link with the following
    response = client.post("/", data={
        "postcode": "SW1A1AA" #does not matter what i put here as its going to take in the fake list anyway
    })

    assert response.status_code==200
    assert b"KFC" in response.data
    assert b"McDonalds" in response.data
    assert b"Burgers" in response.data


#make sure that when we send the postcode - if the api fails we get an error as defined in the code
@patch("backend.restaurant_list")
def test_api_failure(some_data):
    client = app.test_client()

    some_data.side_effect = requests.exceptions.RequestException
    response = client.post("/", data={"postcode": "aaaa"})

    assert response.status_code == 200
    assert b"Something went wrong" in response.data