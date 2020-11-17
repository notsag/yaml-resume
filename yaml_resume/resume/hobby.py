import yaml
import click


class Hobby(yaml.YAMLObject):
    """Class corresponding to a Hobby.

    :param name: The name of the hobby.
    :type name: str
    :param details: More details regarding the hobby.
    :type details: str

    """

    yaml_tag = u"Hobby"

    def __init__(self, name, details):
        self.name = name
        self.details = details

    @staticmethod
    def ask():
        """Interactively create the hobbies section of a resume.

        :returns: A list of Hobby objects.

        """
        hobbies = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("Name")
                details = click.prompt("Details (optional)", default="")
                hobbies.append(Hobby(name, details))
                continue_adding = click.confirm("Add a new hobby?")
            correct = click.confirm("Is this correct?")
        return hobbies

    @staticmethod
    def load(data):
        """Load dictionary and returns a Hobby object.

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: A Hobby object.
        """
        return Hobby(data.get("name"), data.get("details"))
