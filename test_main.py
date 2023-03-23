# import sys
import requests, pytest
from flask import jsonify, Flask

# sys.path.append('/home/guy/Documents/GitHub-UnitTest/Expatriation/api')

baseUrl = 'http://10.10.2.201:5000/'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

def test_status(app):
    with app.app_context():
        path = 'status'
        response = requests.get(baseUrl+path)
        # response.raise_for_status()
        resp = response.json()
        assert resp == "OK"