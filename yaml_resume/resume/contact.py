import yaml
import click


class Location(yaml.YAMLObject):
    """Full address object"""

    yaml_tag = u"Location"

    def __init__(self, address, city, zipcode, state="", country=""):
        self.address = address
        self.city = city
        self.zip = zipcode
        self.state = state
        self.country = country

    def ask():
        """
        Prompt questions for location informations
        returns a Location object
        """
        address = click.prompt("Address")
        city = click.prompt("City")
        zipcode = click.prompt("Zipcode")
        state = click.prompt("State (optional)", default="")
        country = click.prompt("Country (optional)", default="")
        return Location(address, city, zipcode, state, country)


class Contact(yaml.YAMLObject):
    """Contact object"""

    yaml_tag = u"Contact"

    def __init__(self, name, date_of_birth, job, email, phone, location):
        self.name = name
        self.date_of_birth = date_of_birth
        self.job = job
        self.email = email
        self.phone = phone
        self.location = location

    def ask():
        """
        Prompt questions for contact informations
        returns a Contact object
        """
        correct = False
        while not correct:
            name = click.prompt("Full name")
            date_of_birth = click.prompt("Date of birth (dd/mm/yyyy)")
            job = click.prompt("Job title")
            email = click.prompt("Email address")
            phone = click.prompt("Phone number?")
            location = Location.ask()
            correct = click.confirm("Is this correct?")
        return Contact(name, date_of_birth, job, email, phone, location)
