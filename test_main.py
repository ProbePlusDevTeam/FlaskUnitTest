# import api.main
# import json
import requests

baseUrl = "http://127.0.0.1:5000/"

# def test_status():
#    response = main.status()
#    print ("dddddddddddddddddddddddddddddddddddddddddddddddd", response)
# #    assert response
# #    assert response.get("Code") == 200
# test_status()

def test_index():
    response = requests.get(url=baseUrl)
    assert response.status_code == 200

def test_status() :
    path = "status"
    response = requests.get(url=baseUrl+path)
    # responseJson = json.loads(response.text)
    assert response.status_code == 200
    # assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    # assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2


