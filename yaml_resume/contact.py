import yaml
import click


class Location(yaml.YAMLObject):
    """Full address object"""
    yaml_tag = u'Location'

    def __init__(self):
        self.ask_location()

    def ask_location(self):
        self.address = click.prompt("What is your address?")
        self.city = click.prompt("In what city?")
        self.zip = click.prompt("Postal/Zip code of that city?")
        self.state = click.prompt("In what state? (optional)", default="")
        self.country = click.prompt("In what country? (optional)", default="")


class Contact(yaml.YAMLObject):
    """Contact object"""
    yaml_tag = u'Contact'

    def __init__(self):
        self.ask_contact()

    def ask_contact(self):
        """Prompt questions for contact informations"""
        self.name = click.prompt("What is your name?")
        self.job = click.prompt("What is your job title?")
        self.email = click.prompt("What is your email address?")
        self.phone = click.prompt("What is your phone number?")
        self.location = Location()
