"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain):
    try:
        if re.search('http', domain) is not None or re.search('https', domain) is not None:
            return True
        return False
    except TypeError:
        raise Exception("Enter an Integer")


def test_is_http_1():
    domain = 'http://wikipedia.org'
    assert is_http_domain(domain) is True

def test_is_http_2():
    domain = 'https://ru.wikipedia.org/'
    assert is_http_domain(domain) is True

def test_is_http_3():
    domain = 'www.griddynamics.com'
    assert is_http_domain(domain) is False
