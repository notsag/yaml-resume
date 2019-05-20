EMAIL_REGEX = r"(\w+[.|\w])*@(\w+[.])+\w+"
PHONE_NUMBER_REGEX = r"((?:\+|00)[17](?: |\-)?" + \
    r"|(?:\+|00)[1-9]\d{0,2}(?: |\-)?" + \
    r"|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)" + \
    r"|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})" + \
    r"|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]" + \
    r"|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

profile = {
    'network': {'type': 'string'},
    'url': {'type': 'string', 'regex': URL_REGEX},
    }

location = {
    'address': {'type': 'string'},
    'city': {'type': 'string'},
    'state': {'required': False, 'type': 'string'},
    'zip': {'type': 'string'},
    'country': {'required': False, 'type': 'string'},
    }

contact = {
    'name': {'type': 'string'},
    'job': {'type': 'string'},
    'email': {'type': 'string', 'regex': EMAIL_REGEX},
    'phone': {'type': 'string', 'regex': PHONE_NUMBER_REGEX},
    'location': {
        'type': 'dict',
        'required': True,
        'require_all': True,
        'schema': location
        }
    }

resume = {
    'contact': {
        'type': 'dict',
        'required': True,
        'require_all': True,
        'schema': contact
        },
    'profiles': {
        'type': 'list',
        'required': False,
        'require_all': True,
        'schema': {
            'type': 'dict',
            'schema': profile
            }
        }
    }
