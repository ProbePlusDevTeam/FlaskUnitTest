# import sys
import requests, pytest
from flask import Flask

# sys.path.append('/home/guy/Documents/GitHub-UnitTest/Expatriation/api')

baseUrl = 'http://10.10.2.201:5000/'

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
        stat = response.status_code
        print(stat)
        resp = response.json()
        assert stat == 200
        # assert resp == {'status': 'success'}

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
        stat = response.status_code
        print(stat)
        resp = response.json()
        assert resp == {'status': 'exists'}

def test_register_device_empty(app):
    with app.app_context():
        path = 'register_device'
        val = {
            "device_id":None,
            "org_id":None,
            "mfg":None,
            "model":None
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        # assert resp == {'status': 'exists'}
        assert stat == 200

def test_alldevices(app):
    with app.app_context():
        path = 'alldevices'
        val = {
            "org_id":10
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        # assert resp == {'status': 'exists'}
        assert stat == 200

def test_device(app):
    with app.app_context():
        path = 'device'
        val = {
            "device_id":"f0f78a850e4c49be"
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        # assert resp == {'status': 'exists'}
        assert stat == 200

def test_device_grouppolicy(app):
    with app.app_context():
        path = 'device_grouppolicy'
        val = {
            "device_id":"59dddd12db82333d"
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        # resp = response.json()
        # assert resp == {'status': 'exists'}
        assert stat == 200

def test_update_policystatus(app):
    with app.app_context():
        path = 'update_policystatus'
        val = {
            "id":"25",
            "policy_id": 11,
            "ver": 2233,
            "status": True
        }
        response = requests.put(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        assert resp == {'status': 'success'}
        
def test_delete_device(app):
    with app.app_context():
        path = 'delete_device'
        val = {
            "id": "33"
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        assert resp == {'status': 'success'}

def test_group_device(app):
    with app.app_context():
        path = 'group_device'
        val = {
            "group_id":"90", 
            "devices": [25, 26]
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        assert resp == {'status': 'success'}