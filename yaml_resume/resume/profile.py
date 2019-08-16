import yaml
import click


class Profile(yaml.YAMLObject):
    """Profile object"""

    yaml_tag = u"Profile"

    def __init__(self, network, url):
        self.network = network
        self.url = url

    def ask():
        """
        Prompt questions for profiles section
        returns a list of Profiles object
        """
        profiles = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                network = click.prompt("Network")
                url = click.prompt("URL")
                profiles.append(Profile(network, url))
                continue_adding = click.confirm("Add a new profile?")
            correct = click.confirm("Is this correct?")
        return profiles
