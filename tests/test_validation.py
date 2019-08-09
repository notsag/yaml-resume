import re
from yaml_resume.validator import schema

DOB = {
    'valid': [
        '01/10/1990',
        '20/10/1990',
        '20/01/1990',
        '30/01/1990',
        '1/10/1990',
        '1/10/1990',
        ],
    'not_valid': [
        '01/13/90',
        '01/10/90',
        '40/10/1990',
        '10/40/1990',
        ]
    }

EMAILS = {
    'valid': [
        'john@doe.com',
        'john.doe@johndoe.com',
        'john@doe.co.uk'
        ],
    'not_valid': [
        'johndoe.com',
        'john.doe@johndoe',
        ]
    }

URLS = {
    'valid': [
        'http://sbook.com/johndoe',
        'https://sbook.com/johndoe',
        ],
    'not_valid': [
        'sbook.com/johndoe',
        'ftp://sbook.com/johndoe',
        ]
    }

PHONE_NUMBERS = {
    'valid': [
        '+33 00 00 00 00 00',
        '+330000000000',
        '+33000000000',
        '0600000000',
        '06 00 00 00 00',
        '555-000-0000',
        ],
    'not_valid': [
        '000',
        'a0000000',
        '00 00 00'
        ]
    }


def test_email_validation():
    for email in EMAILS['valid']:
        assert re.match(schema.EMAIL_REGEX, email)
    for email in EMAILS['not_valid']:
        assert not re.match(schema.EMAIL_REGEX, email)


def test_valid_phone_numbers():
    for nu in PHONE_NUMBERS['valid']:
        assert re.match(schema.PHONE_NUMBER_REGEX, nu)
    for nu in PHONE_NUMBERS['not_valid']:
        assert not re.match(schema.PHONE_NUMBER_REGEX, nu)


def test_valid_urls():
    for url in URLS['valid']:
        assert re.match(schema.URL_REGEX, url)
    for url in URLS['not_valid']:
        assert not re.match(schema.URL_REGEX, url)


def test_date_of_birth():
    for dob in DOB['valid']:
        assert re.match(schema.DOB_REGEX, dob)
    for dob in DOB['not_valid']:
        assert not re.match(schema.DOB_REGEX, dob)
