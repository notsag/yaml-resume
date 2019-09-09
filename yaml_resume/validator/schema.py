DOB_REGEX = r"(([0-2][0-9])|[1-9]|(3[0-1]))/((1[0-2])|(0?[1-9]))/[0-9]{4}"
EMAIL_REGEX = r"(\w+[.|\w])*@(\w+[.])+\w+"
PHONE_NUMBER_REGEX = (
    r"((?:\+|00)[17](?: |\-)?"
    + r"|(?:\+|00)[1-9]\d{0,2}(?: |\-)?"
    + r"|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)"
    + r"|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})"
    + r"|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
)
URL_REGEX = (
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]"
    + r"|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

experience = {
    "company": {"type": "string"},
    "position": {"type": "string"},
    "start_date": {"type": "string"},
    "end_date": {"type": "string", "required": False},
    "summary": {"type": "string"},
    "tags": {"type": "list", "schema": {"type": "string"}},
    "website": {"type": "string", "regex": URL_REGEX, "required": False},
}

degree = {
    "institution": {"type": "string"},
    "degree": {"type": "string"},
    "start_date": {"type": "string"},
    "end_date": {"type": "string", "required": False},
    "website": {"type": "string", "regex": URL_REGEX, "required": False},
}

skill = {"name": {"type": "string"}, "level": {"type": "integer", "min": 0, "max": 100}}

hobby = {"name": {"type": "string"}, "details": {"type": "string", "required": False}}

project = {
    "name": {"type": "string"},
    "description": {"type": "string"},
    "url": {"type": "string", "regex": URL_REGEX, "required": False},
}

language = {"name": {"type": "string"}, "level": {"type": "string"}}

profile = {"network": {"type": "string"}, "url": {"type": "string", "regex": URL_REGEX}}

location = {
    "address": {"type": "string"},
    "city": {"type": "string"},
    "state": {"required": False, "type": "string"},
    "zip": {"type": "string"},
    "country": {"required": False, "type": "string"},
}

contact = {
    "name": {"type": "string"},
    "job": {"type": "string"},
    "date_of_birth": {"type": "string", "regex": DOB_REGEX},
    "email": {"type": "string", "regex": EMAIL_REGEX},
    "phone": {"type": "string", "regex": PHONE_NUMBER_REGEX},
    "location": {
        "type": "dict",
        "required": True,
        "require_all": True,
        "schema": location,
    },
}

resume = {
    "contact": {
        "type": "dict",
        "required": True,
        "require_all": True,
        "schema": contact,
    },
    "profiles": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": profile},
    },
    "experiences": {
        "type": "list",
        "required": True,
        "require_all": True,
        "schema": {"type": "dict", "schema": experience},
    },
    "education": {
        "type": "list",
        "required": True,
        "require_all": True,
        "schema": {"type": "dict", "schema": degree},
    },
    "skills": {
        "type": "list",
        "required": True,
        "require_all": True,
        "schema": {"type": "dict", "schema": skill},
    },
    "languages": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": language},
    },
    "projects": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": project},
    },
    "hobbies": {
        "type": "list",
        "required": False,
        "require_all": False,
        "schema": {"type": "dict", "schema": hobby},
    },
}
