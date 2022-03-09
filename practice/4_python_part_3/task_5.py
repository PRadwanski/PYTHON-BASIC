"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
import requests

def make_request(address):
    req = requests.get(address)
    code = req.status_code
    response = req.encoding

    return code, response

@pytest.fixture
def address():
    return make_request('https://www.google.com')

def test_make_request_1(address):
    assert type(address) == tuple

def test_make_request_2(address):
    assert address == (200, 'ISO-8859-1')
