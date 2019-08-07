import re
from yaml_resume.validator import schema

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
