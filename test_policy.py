import requests, pytest
from flask import Flask

baseUrl = 'http://10.10.2.201:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def test_allpolicies(app):
    with app.app_context():
        path = 'allpolicies'
        val = {
            "org_id":0
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert stat == 200
        # assert resp == {'status': 'success'}

def test_addpolicy(app):
    with app.app_context():
        path = 'addpolicy'
        val = {
            "pname": "UT-Policy 123",
            "desc": "This is Unit Test policy",
            "org_id": 0,
            "access": 0,
            "usb": 0,
            "sys_apps": "{ 'settings':'0', 'filemanager': '0', 'browser': '0', 'dialer': '0' }",
            "custom_apps": "{}"
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'success'}

def test_delete_policy(app):
    with app.app_context():
        path = 'delete_policy'
        val = {
            "id": 22,
            "org_id": 0
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'success'}