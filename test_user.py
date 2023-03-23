import requests, pytest
from flask import Flask
import sys
import mysql.connector
from dotenv import load_dotenv
import os

#change the path to your .env file
load_dotenv(dotenv_path='/home/guy/Documents/GitHub-probeplus/.env')

host = os.getenv('mysql_HOST')
username = os.getenv('mysql_USERNAME')
password = os.getenv('mysql_PASSWORD')
db = os.getenv('mysql_DATABASE')

print(host, username, password, db)

baseUrl = 'http://10.10.2.221:5000/'

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
    connection = create_connection(host, username,password,db)
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
    query = "INSERT INTO users (id, user_name, password, first_name, last_name, mobile_number, country_code, email, sup_id, org_id, c_id, role, policy, created_at, updated_at) VALUES(5, 'test', 'test', '', '', '2147483647', 0, 'test@test.com', 0, 10, '0', 3, 'asd', '2023-02-16 16:35:31', '2023-02-16 16:35:31')"
    result = execute_query(query)
    print("Setup: ", result)

def theteardown():
    query = "TRUNCATE TABLE users;"
    result = execute_query(query)
    print("Teardown: ", result)

@pytest.fixture(scope="session")
def environment(request):
    print("initial")
    thesetup()
    def fin():
        theteardown()
    request.addfinalizer(fin)

# def test_adduser(app, environment):
#     with app.app_context():
#         path = 'adduser'
#         val = {
#             "username": "user2",
#             "password": "user123",
#             "email": "user@probeplus.in",
#             "role": 0,
#             "org_id": 10,
#             "mobile_number": "9123456789"
#         }
#         response = requests.post(baseUrl+path, json=val)
#         stat = response.status_code
#         print(stat)
#         resp = response.json()
#         assert resp == {'status': 'success'}
        # assert stat == 200

# def test_getuser(app, environment):
#     with app.app_context():
#         path = 'getuser'
#         val = {
#             "username":"user2"
#         }
#         response = requests.post(baseUrl+path, json=val)
#         stat = response.status_code
#         print(stat)
#         resp = response.json()
#         print(resp)
#         assert stat == 200

# def test_delete_user(app, environment):
#     with app.app_context():
#         path = 'delete_user'
#         val = {
#             "username":"user2"
#         }
#         response = requests.post(baseUrl+path, json=val)
#         stat = response.status_code
#         print(stat)
#         resp = response.json()
#         assert resp == {'status': 'success'}

def test_allusers(app, environment):
    with app.app_context():
        path = 'allusers'
        response = requests.get(baseUrl+path)
        stat = response.status_code
        print(stat)
        resp = response.json()
        print(resp)
        assert stat == 200