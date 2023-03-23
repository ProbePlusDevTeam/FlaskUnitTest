# import sys
import requests, pytest
from flask import Flask
import mysql.connector


baseUrl = 'http://10.10.3.115:5000/'

host="127.0.0.1"
user="root"
passwd="password"
db="pp_mdm_ut"

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def create_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            db=database
        )
        print("connected")
    except mysql.connector.Error as e:
        data = str(e)
        result = {}
        result["status"]= "failure"
        result["error"]= data
        return result

    return connection

def execute_query(query):
    connection = create_connection(host, user,passwd,db)
    cursor = connection.cursor()
    result = None
    print("inside execute query")
    try:
        cursor.execute(query)
        print("executed now")
        result = {}
        result["status"]= "success"
        return result
    except mysql.connector.Error as e:
        data = str(e)
        result = {}
        result["status"]= "failure"
        result["error"]= data
        return result

def thesetup():
    # with app.app_context():
    #     path = 'register_device'
    #     val = {
    #         "device_id":"f0f78a850e4c49b8",
    #         "org_id":10,
    #         "mfg":"Xiaomi",
    #         "model":"Redmi K20 Pro"
    #     }
    #     response = requests.post(baseUrl+path, json=val)
    #     stat = response.status_code
    #     print(stat)
    #     resp = response.json()
        # print("Setup: ", resp)

    query = "SELECT * FROM devices;"
    result = execute_query(query)
    print("Setup1: ", result)

def theteardown():
    query = "TRUNCATE TABLE devices;"
    result = execute_query(query)
    print("Teardown: ", result)

# @pytest.fixture(scope="session")
def environment(request):
    print("initial")
    thesetup()
    def fin():
        theteardown()
    request.addfinalizer(fin)

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