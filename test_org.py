import requests, pytest
from flask import Flask

baseUrl = 'http://10.10.2.201:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def test_allorgs(app):
    with app.app_context():
        path = 'allorgs'
        val = {
            "p_id":10
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert stat == 200
        # assert resp == {'status': 'success'}

# The UserId should be present in User Table and it should contain child ids in "c_id" column
def test_allorgsforuser(app):
    with app.app_context():
        path = 'allorgsforuser'
        val = {
            "user_id":6
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert stat == 200
        # assert resp == {'status': 'success'}