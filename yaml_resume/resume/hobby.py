import yaml
import click


class Hobby(yaml.YAMLObject):
    """Hobby object"""

    yaml_tag = u"Hobby"

    def __init__(self, name, details):
        self.name = name
        self.details = details

    def ask():
        """
        Prompt questions for hobbies section
        returns a list of Hobby objects
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
