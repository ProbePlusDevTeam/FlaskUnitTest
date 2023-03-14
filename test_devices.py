import sys
import requests, pytest
from flask import jsonify, Flask

# sys.path.append('/home/guy/Documents/GitHub-UnitTest/Expatriation/api')

baseUrl = 'http://10.10.3.219:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def test_register_device_new(app):
    with app.app_context():
        path = 'register_device'
        val = {
            "device_id":"59dddsdfqay2333d",
            "org_id":10,
            "mfg":"Xiaomi",
            "model":"Redmi 12 pro"
        }
        response = requests.post(baseUrl+path, json=val)
        e = response.status_code
        print(e)
        resp = response.json()
        assert resp == {'status': 'success'}

def test_register_device_exist(app):
    with app.app_context():
        path = 'register_device'
        val = {
            "device_id":"59dddd13qay2333d",
            "org_id":10,
            "mfg":"Xiaomi",
            "model":"Redmi 12 pro"
        }
        response = requests.post(baseUrl+path, json=val)
        e = response.status_code
        print(e)
        resp = response.json()
        assert resp == {'status': 'exists'}

# def test_alldevices(app)