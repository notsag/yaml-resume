import yaml
import click


class Profile(yaml.YAMLObject):
    """Class corresponding to a profile on social network.

    :param network: The name of the network.
    :type network: str
    :param url: The url of the profile.
    :type url: str

    """

    yaml_tag = u"Profile"

    def __init__(self, network, url):
        self.network = network
        self.url = url

    @staticmethod
    def ask():
        """Interactively create a Profile object.

        :returns: A Profile object from privided answers.

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

    @staticmethod
    def load(data):
        """Load dictionary and returns a Profile object

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: A Profile object.
        """
        return Profile(data.get("network"), data.get("url"))
