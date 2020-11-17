import yaml
import click


class Language(yaml.YAMLObject):
    """Class corresponding to a language.

    :param name: The name of the language.
    :type name: str
    :param level: The level for this language.
    :type level: str

    """

    yaml_tag = u"Language"

    def __init__(self, name, level):
        self.name = name
        self.level = level

    @staticmethod
    def ask():
        """Interactively create the language section of the resume.

        :returns: A list of Language objects.

        """
        languages = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("Language")
                level = click.prompt("Level")
                languages.append(Language(name, level))
                continue_adding = click.confirm("Add a new language?")
            correct = click.confirm("Is this correct?")
        return languages

    @staticmethod
    def load(data):
        """Load dictionary and returns an Language object.

        :params data: A dictionary that should come from a yaml file.
        :type data: dict[]
        :returns: A Language object.

        """
        return Language(data.get("name"), data.get("level"))
