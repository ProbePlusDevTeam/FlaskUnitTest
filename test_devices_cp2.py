import requests, pytest
from flask import Flask
import sys
import mysql.connector
from dotenv import load_dotenv
import os
sys.path.append('/home/guy/Documents/GitHub-probeplus/Expatriation/api')
# from api 
import config
import db


#change the path to your .env file
# load_dotenv(dotenv_path='/home/guy/Documents/GitHub-probeplus/.env')

# host = os.getenv('mysql_HOST')
# username = os.getenv('mysql_USERNAME')
# password = os.getenv('mysql_PASSWORD')
# db = os.getenv('mysql_DATABASE')

# print(host, username, password, db)

baseUrl = 'http://10.10.3.115:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def thesetup():
    query = "INSERT INTO devices (id, user_name, password, first_name, last_name, mobile_number, country_code, email, sup_id, org_id, c_id, role, policy, created_at, updated_at) VALUES(5, 'test', 'test', '', '', '2147483647', 0, 'test@test.com', 0, 10, '0', 3, 'asd', '2023-02-16 16:35:31', '2023-02-16 16:35:31')"
    result = db.execute_query(query)
    print("Setup: ", result)

# def theteardown():
#     query = "TRUNCATE TABLE devices;"
#     result = execute_query(query)
#     print("Teardown: ", result)

def setup_module(module):
    print('\nSetup of module is called')
    # thesetup()
    query = "SELECT * FROM devices;"
    result = db.execute_read_query(query)
    print("Setup1: ", result)
    # def fin():
    #     theteardown()
    # request.addfinalizer(fin)

def teardown_module(module):
    print('\nTeardown of module is called')
    # query = "TRUNCATE TABLE devices;"
    # result = execute_query(query)
    # print("Teardown: ", result)

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
        # assert resp == {'status': 'success'}
        assert resp == {'status': 'failure'}

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