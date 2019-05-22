import yaml
import click


class Location(yaml.YAMLObject):
    """Full address object"""
    yaml_tag = u'Location'

    def __init__(self, address, city, zipcode, state="", country=""):
        self.address = address
        self.city = city
        self.zip = zipcode
        self.state = state
        self.country = country

    def ask_location():
        """
        Prompt questions for location informations
        returns a Location object
        """
        address = click.prompt("What is your address?")
        city = click.prompt("In what city?")
        zipcode = click.prompt("Postal/Zip code of that city?")
        state = click.prompt("In what state? (optional)", default="")
        country = click.prompt("In what country? (optional)", default="")
        return Location(address, city, zipcode, state, country)


class Contact(yaml.YAMLObject):
    """Contact object"""
    yaml_tag = u'Contact'

    def __init__(self, name, job, email, phone, location):
        self.name = name
        self.job = job
        self.email = email
        self.phone = phone
        self.location = location

    def ask_contact():
        """
        Prompt questions for contact informations
        returns a Contact object
        """
        correct = False
        while not correct:
            name = click.prompt("What is your name?")
            job = click.prompt("What is your job title?")
            email = click.prompt("What is your email address?")
            phone = click.prompt("What is your phone number?")
            location = Location.ask_location()
            correct = click.confirm("Is this correct?")
        return Contact(name, job, email, phone, location)
