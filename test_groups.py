import requests, pytest
from flask import Flask

baseUrl = 'http://10.10.2.201:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def test_allgroups(app):
    with app.app_context():
        path = 'allgroups'
        val = {
            "org_id":11
        }
        response = requests.post(baseUrl+path, json=val)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        # assert resp == {'status': 'success'}
        assert stat == 200

def test_addgroup(app):
    with app.app_context():
        path = 'addgroup'
        val = {
            "gname": "Java",
            "desc": "Have a cup",
            "org_id": 10,
            "policy_id": 13
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'success'}

def test_updategroup(app):
    with app.app_context():
        path = 'updategroup'
        val = {
            "gname": "St. John's Hospital",
            "desc": "Do good and do it well.",
            "group_id": 7,
            "policy_id": 13
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'success'}

# Test updategroup api for a Group that's not present in device table
def test_updategroup2(app):
    with app.app_context():
        path = 'updategroup'
        val = {
            "gname": "St. James Hospital",
            "desc": "Shine bright",
            "group_id": 9,
            "policy_id": 13
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'failure'}

def test_delete_group(app):
    with app.app_context():
        path = 'delete_group'
        val = {
            "id": 23,
            "org_id": 10
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert resp == {'status': 'success'}

def test_device_policy(app):
    with app.app_context():
        path = 'device_policy'
        val = {
            "group_id": "23"
        }
        response = requests.post(baseUrl+path, json=val)
        # response = requests.post(baseUrl+path, json={})
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert stat == 200
