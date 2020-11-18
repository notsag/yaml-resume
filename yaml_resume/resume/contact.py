import yaml
import click


class Location(yaml.YAMLObject):
    """Class corresponding to an full address.

    :param address: Street number and name.
    :type address: str
    :param city: City name.
    :type city: str
    :param zip: Zip/Postal code
    :type zip: str
    :param state: (`optional`) State.
    :type state: str
    :param country: (`optional`) Country name or code.
    :type country: str

    """

    yaml_tag = u"Location"

    def __init__(self, address, city, zipcode, state="", country=""):
        self.address = address
        self.city = city
        self.zip = zipcode
        self.state = state
        self.country = country

    @staticmethod
    def ask():
        """Interactively create a Location object.

        :returns: a Location object

        """
        address = click.prompt("Address")
        city = click.prompt("City")
        zipcode = click.prompt("Zipcode")
        state = click.prompt("State (optional)", default="")
        country = click.prompt("Country (optional)", default="")
        return Location(address, city, zipcode, state, country)

    @staticmethod
    def load(data):
        """Load dictionary and returns a Location object.

        :param data: A dictionary corresponding to a Location object.
        :type data: dict[]
        :returns: A Location object.
        """
        return Location(
            data.get("address"),
            data.get("city"),
            data.get("zip"),
            data.get("state"),
            data.get("country"),
        )


class Contact(yaml.YAMLObject):
    """Class corresponding to the contact section of a resume.

    :param name: The first, middle and last name.
    :type name: str
    :param date_of_birth: The date of birth.
    :type date_of_birth: str
    :param job: The current or researched position.
    :type job: str
    :param summary (`optional`): The carreer summary.
    :type summary: str
    :param email: An email address.
    :type email: str
    :param phone: The phone number.
    :type phone: str
    :param location: The full address.
    :type location: Location

    """

    yaml_tag = u"Contact"

    def __init__(self, name, date_of_birth, job, summary, email, phone, location):
        self.name = name
        self.date_of_birth = date_of_birth
        self.job = job
        self.summary = summary
        self.email = email
        self.phone = phone
        self.location = location

    @staticmethod
    def ask():
        """Interactively create a Contact object.

        :returns: a Contact object.
        """
        correct = False
        while not correct:
            name = click.prompt("Full name")
            date_of_birth = click.prompt("Date of birth (dd/mm/yyyy)")
            job = click.prompt("Job title")
            summary = click.prompt("Career summary (optional)", default="")
            email = click.prompt("Email address")
            phone = click.prompt("Phone number")
            location = Location.ask()
            correct = click.confirm("Is this correct?")
        return Contact(name, date_of_birth, job, summary, email, phone, location)

    @staticmethod
    def load(data):
        """Load dictionary and returns a Contact object.

        :param data: A dictionary corresponding to a contact object.
        :type data: dict[]
        :returns: A Contact object.

        """
        return Contact(
            data.get("name"),
            data.get("date_of_birth"),
            data.get("job"),
            data.get("summary"),
            data.get("email"),
            data.get("phone"),
            Location.load(data.get("location")),
        )
